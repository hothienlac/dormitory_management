const reply_markup = {
    inline_keyboard: [
        [{
            text: '<< Main Menu',
            callback_data: 'mainMenu',
        }]
    ]
}

const text = '=== ACTIVITIES ===\n\nActivities feature is not available now!';

module.exports = {reply_markup, text};