const { authenticate, xbl } = require('@xboxreplay/xboxlive-auth');
const { call, getPlayerXUID } = require('@xboxreplay/xboxlive-api');
const { writeFileSync } = require('fs');
const args = require('yargs').argv;
let config, response, deviceDetails;

const nullactivity = {
  details: "",
  state: "",
  device: "",
  game: ""
};

const jsonfile = __dirname + '/rpc.json';

async function richPresence(username, password){
  const XBLContractVersion = 1;
  // Get Xbox credentials 
  const { Token: deviceToken } = await xbl.EXPERIMENTAL_createDummyWin32DeviceToken();
  const { user_hash, xsts_token } = await authenticate(username, password, {
    deviceToken
  });
  const userID = args.xuid;
  config = {
    url: `https://peoplehub.xboxlive.com/users/me/people/xuids(${userID})/decoration/presenceDetail`,
    method: 'GET'
  };
  const authorization = {
    userHash: user_hash,
    XSTSToken: xsts_token
  };
  try{
    response = await call(config, authorization, XBLContractVersion);

    // Presence info
    let presenceText = response['people'][0]['presenceDetails'], device;

    if(presenceText == undefined){
      presenceText = ["undefined", "undefined", "undefined"];
      device = "undefined";
    }
    else if(presenceText){
      i = 0;
      let j;
      while(i < presenceText.length){
        console.log(response['people'][0]['presenceDetails'][i]);
        if(response['people'][0]['presenceDetails'][i]['Device'] == "Win32"){
          j = i;
          i = presenceText.length;
          presenceText = response['people'][0]['presenceDetails'][j]['PresenceText'].split(" - ");
          device = response['people'][0]['presenceDetails'][j]['Device'];

          const activity = {
            details: presenceText[2],
            state: presenceText[1],
            device: device,
            game: presenceText[0]
          };
          console.log(activity);
          try{
            writeFileSync(jsonfile, JSON.stringify(activity, null, 2));
          }
          catch(err){
            console.log("Unable to write to file. Check to make sure all data entered is correct.")
          }
        }
        i += 1;
      }
    }
  }
  catch(err){
    console.log("Check and see if you are running Halo: MCC");
    console.log(err)
    writeFileSync(jsonfile, JSON.stringify(nullactivity, null, 2));
  }
    return;
}
richPresence(args.u, args.p);

/**
 * args.u, args.p
    steamid: "76561198293744031",
    gameid: "976730",
    lobbysteamid: "109775241013106433"
    steam://joinlobby/
    976730/                             <------ Game ID
    109775241013106433/                 <------ Lobby ID
    76561198293744031                   <------ Steam ID
    80EC429274AF252714363656B71562C0    <------ API Key
 */

//   const defaultData = {
//      "details": null,
//      "state": null,
//      "assets":{
//          "largeImageKey": null,
//          "largeImageText": null,
//          "smallImageKey": null,
//          "smallImageText": null
//      }
//    }
//  }
  
  // fs.writeFile("./rpc.json", JSON.stringify(defaultData), err => {
  //   if (err) console.log('Error writing file:', err)
  // });