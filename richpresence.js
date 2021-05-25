const { authenticate, xbl } = require('@xboxreplay/xboxlive-auth');
const { call } = require('@xboxreplay/xboxlive-api');
const { writeFileSync, readFileSync } = require('fs');
const args = require('yargs').argv;
const { option } = require('yargs');
let config, response, deviceDetails;

const nullactivity = {
  details: "",
  state: "",
  device: "",
  game: ""
};

const jsonfile = __dirname + '/rpc.json';


async function richPresence(){
  // Get Xbox credentials 
  const data = JSON.parse(readFileSync((__dirname + "/tokens/xtoken.json")));
  const authorization = {
    userHash: data['DisplayClaims']['xui'][0]['uhs'],
    XSTSToken: data['Token'], 
    xuid: data['DisplayClaims']['xui'][0]['xid']
  };
  config = {
    url: `https://peoplehub.xboxlive.com/users/me/people/xuids(${authorization.xuid})/decoration/presenceDetail`,
    method: 'GET'
  };
  try{
    response = await call(config, authorization, 1);

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
        if((response['people'][0]['presenceDetails'][i]['PresenceText'].startsWith("Halo: The Master Chief Collection -"))){

          presenceText = response['people'][0]['presenceDetails'][i]['PresenceText'].split(" - ");
          console.log(presenceText);
          device = response['people'][0]['presenceDetails'][i]['Device'];
          
          i = presenceText.length;

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
            console.log(err)
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
richPresence();

/**
 * args.u, args.p
    steamid: "",
    gameid: "976730",
    lobbysteamid: ""
    steam://joinlobby/
    976730/                             <------ Game ID
    lobbysteamid/                       <------ Lobby ID
    steamid                             <------ Steam ID
    80EC429274AF252714363656B71562C0    <------ API Key
 */