def final_total(first, second, service_fee):
    koko =  first + second + service_fee
    print(koko)
    

@ -8,7 +8,6 @@
	# Example:
	
	# participant_cost(10, 800, 200) => 10000
	
	def participant_cost (attendees, food_per_person, transport_per_person):
	    return attendees * (food_per_person + transport_per_person)
	
	@ -19,6 +18,8 @@ print(participant_cost(10, 800, 200))
	print(participant_cost(0, 800, 200))
	
	
	
	
	#Second component
	# B. event_total
	
	@ -44,11 +45,7 @@ print(event_total(0, 800, 200, 5000))
	    
	
	
	
	
	#third component
	
	
	# C. budget_status
	
	# Return "Within budget" when:
	@ -76,6 +73,8 @@ print(budget_status(15000, 15000))
	print(budget_status(15000, 150000))
	
	
	
	
	#fourth component
	# D. event_summary
	
	@ -84,13 +83,29 @@ print(budget_status(15000, 150000))
	# Required pattern:
	
	# Study Day: total 15000 naira. Within budget.
	
	def event_summary(event_name, total, status):
	    return f"{event_name}: total {total} naira. {status}"
	
	#Normal case required Study Day example
	
	print(event_summary("Study Day", event_total(10,800,200,5000), budget_status(15000,15000)))
	
	#one different event name and total.
	print(event_summary("Assessment", event_total(20,800,200,4000), budget_status(15000,15000)))
	
	
	
	
	
	# Full Acceptance case 
	people = participant_cost(10, 800, 200)
	total = event_total(10, 800, 200, 5000)
	status = budget_status(16000, total)
	summary = event_summary("Study Day", total, status)
	
	# Prints the text followed by 5 newlines
	print("\nfull Acceptance case")
	
	print(f"people: {people}")
	print(f"total: {total}")
	print(f"status: {status}")
	print(f"summary: {summary}")