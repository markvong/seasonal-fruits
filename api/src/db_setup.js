const fs        = require('fs');
const mongoose  = require('mongoose');
const db        = require('./db');
const { exit }  = require('process');
require('dotenv').config();

mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true, useUnifiedTopology: true 
})
.then(() => {
    console.log(`connected to ${process.env.MONGO_URI}`);
    // updateSeasonNamesData();
    // updateStateNamesData();
    updateStateData(() => console.log('finished'));
})
.catch(err => console.log(`error occurred: ${err}`));

const seasonFilePath = 'data/modeled_data.json';
const fruitFilePath = 'data/fruit_list.json';

function readFile(path) {
    var rawdata = fs.readFileSync(path);
    var seasonalFruitsData = JSON.parse(rawdata);
    return seasonalFruitsData;
}

function updateStateData(callback) {
    var scrapedData = readFile(seasonFilePath);
    var fruitData = readFile(fruitFilePath);
    var statesArray = [];
    for (const stateName in scrapedData) {
        var stateData = scrapedData[stateName];
        var seasonsArray = [];
        stateData['seasons'].forEach((seasonData) => {
            var fruitDocList = [];
            seasonData['fruits'].forEach(fruit => {
                var fruitDoc = new db.Fruit({
                    name: fruit,
                    description: fruitData[fruit.toLowerCase()]
                });
                fruitDocList.push(fruitDoc);
            });
            var seasonDoc = new db.Season({
                season: seasonData['season'],
                fruits: fruitDocList
            });
            seasonsArray.push(seasonDoc);
        });

        var stateDoc = new db.State({
            state: stateName,
            seasons: seasonsArray
        });
        statesArray.push(stateDoc);
    }
    db.State.insertMany(statesArray, (err, docs) => {   
        if (err) console.log(err);
        else console.log(docs);
    });
    callback();
}

function updateStateNamesData() {
    var scrapedData = readFile();
    var statesNameArray = [];
    for (const stateName in scrapedData) {
        console.log(stateName);
        var stateNameDoc = new db.StateName({
            stateName: stateName
        });
        statesNameArray.push(stateNameDoc);
    }
    console.dir(statesNameArray);
    StateName.insertMany(statesNameArray, (err, docs) => {
        if (err) console.log(err);
        else console.log(docs);
    });    
}

function updateSeasonNamesData() {
    var scrapedData = readFile();
    var seasonNameArray = [];
    // just need one state
    for (const seasonData in scrapedData['Alaska']['seasons']) {
        const seasons = scrapedData['Alaska']['seasons'];
        console.log(seasons[seasonData]['season']);
        var seasonNameDoc = new db.SeasonName({
            seasonName: seasons[seasonData]['season']
        });
        seasonNameArray.push(seasonNameDoc);
    }
    console.dir(seasonNameArray);
    SeasonName.insertMany(seasonNameArray, (err, docs) => {
        if (err) console.log(err);
        else console.log(docs);
    });

}
// updateStateData(exit);
// updateStateNamesData();
// updateSeasonNamesData();
