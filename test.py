from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent


# res = tavily_search("Best hotel in india")
# print(res)


# res = search_flights("Plan 7 day Nepal trip from bangladesh")
# print(res)

user_input = input("Enter Travel Request :  ")

resp = run_travel_agent(
    user_input=user_input,
    thread_id="test_user")

print("\nFINAL RESPONSE:\n")
print(resp['answer'])