.mode "csv"
.separator ","

.import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/animal.csv"' animal
.import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/animals_assistant.csv"' animals_assistant
.import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/shelter_assistant.csv"' shelter_assistant
.import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/shelter.csv"' shelter
.import '| tail -n +2 "/Users/christian-john/Downloads/CSE111/project/Project_Phase2/data/status.csv"' status