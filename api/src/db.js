const mongoose = require('mongoose');

const seasonSchema = mongoose.Schema({
    season: { type: String, required: true },
    fruits: [String]
});

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
    StateName,
    SeasonName,
    State
}