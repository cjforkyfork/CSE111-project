.mode "csv"
.separator ","

.import '| tail -n +2 "/Users/amelc/OneDrive/Desktop/Phase3/CSE111-project/Project_Phase2/data/animal.csv"' animal
.import '| tail -n +2 "animals_assistant.csv"' animals_assistant

.import '| tail -n +2 "city.csv"' city
.import '| tail -n +2 "customer_community.csv"' customer_community
.import '| tail -n +2 "customer.csv"' customer

.import '| tail -n +2 "donations.csv"' donations
.import '| tail -n +2 "requests.csv"' requests_visits
.import '| tail -n +2 "shelter_assistant.csv"' shelter_assistant

.import '| tail -n +2 "shelter.csv"' shelter
.import '| tail -n +2 "status.csv"' status
.import '| tail -n +2 "visits.csv"' visits

.import '| tail -n +2 "animal.csv"' animal

-- Deletes
-- DELETE FROM animals_assistant