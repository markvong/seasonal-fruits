const mongoose = require('mongoose');

const fruitSchema = mongoose.Schema({
    name: String,
    description: String
});
const Fruit = mongoose.model('Fruit', fruitSchema);

const seasonSchema = mongoose.Schema({
    season: { type: String, required: true },
    fruits: { type: [fruitSchema] }
});
const Season = mongoose.model('Season', seasonSchema);

const stateSchema = mongoose.Schema({
    state: { type: String, required: true },
    seasons: { type: [seasonSchema] }
});
const State = mongoose.model('State', stateSchema);

const stateNameSchema = mongoose.Schema({
    stateName: { type: String, required: true }
});
const StateName = mongoose.model('StateName', stateNameSchema);

const seasonNameSchema = mongoose.Schema({
    seasonName: { type: String, required: true }
});
const SeasonName = mongoose.model('SeasonName', seasonNameSchema);

module.exports = {
    Fruit,  
    StateName,
    SeasonName,
    Season,
    State
}