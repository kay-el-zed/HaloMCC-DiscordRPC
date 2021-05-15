const { authenticate, xbl } = require('@xboxreplay/xboxlive-auth');
const { call } = require('@xboxreplay/xboxlive-api');
const { writeFileSync } = require('fs');
const args = require('yargs').argv;
let config, response, deviceDetails;


async function richPresence(username, password){
  const startTimestamp = new Date();
  const XBLContractVersion = 1;
  // Get Xbox credentials 
  const { Token: deviceToken } = await xbl.EXPERIMENTAL_createDummyWin32DeviceToken();
  const { user_hash, xsts_token } = await authenticate(username, password, {
    deviceToken
  });
  config = {
    url: `https://peoplehub.xboxlive.com/users/me/people/xuids(2535457457644552)/decoration/presenceDetail`,
    method: 'GET'
  };
  const authorization = {
    userHash: user_hash,
    XSTSToken: xsts_token
  };
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
      response['people'][0]['presenceDetails'][i];
      if(response['people'][0]['presenceDetails'][i]['PresenceText'].startsWith("Halo: The Master Chief Collection")){
        j = i;
        i = presenceText.length;
        presenceText = response['people'][0]['presenceDetails'][j]['PresenceText'].split(" - ");
        device = response['people'][0]['presenceDetails'][j]['Device'];
        // console.log(device);
        // console.log(presenceText[0]);
        // console.log(presenceText[1]);
        // console.log(presenceText[2]);
        const activity = {
          details: presenceText[2],
          state: presenceText[1],
          device: device,
          game: presenceText[0]
        }
        console.log(activity);
        writeFileSync("./rpc.json", JSON.stringify(activity, null, 2));
      }
      i += 1;
    }
  }
    return;
}
richPresence(args.u, args.p);

/**
 * 
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
