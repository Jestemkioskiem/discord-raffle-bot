# config.py

# List of roles that will be able to initialize raffles and will not be considered for winning one. 
permitted_roles = [
'broadcaster', # default value
]

# List of ready messages for the bot to utilize in the code.
r_messages = {
	"raffle_start" : "<@{}> has initiated a raffle! Type something in the chat in the next {} minutes to participate! The prize set for this raffle is '{}'!",
	"raffle_ending" : "There are only {} minute(s) remaining for <@{}>'s raffle! Type something in the chat if you wish to participate!",
	"raffle_end" : "The raffle has ended! The winner will be announced after I'm done counting!",
	"raffle_winner" : "<@{}> is the winner of the raffle initiated by <@{}>! Congratulations! The prize set for this raffle was '{}'!",
	"raffle_error_arguments" : "Sorry <@{}>, seems like you haven't passed enough arguments in! Type in '!raffle *time_in_minutes* *the_prize*!'",
	"raffle_error_time" : "Sorry <@{}>, I can only hold raffles between 10 and 30 minutes long!",
	"raffle_result_dm" : "List of the IDs of the participants: {}. Type in '<@id>' to tag the user if needed."
}
