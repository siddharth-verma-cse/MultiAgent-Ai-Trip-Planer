from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


# res = tavily_search("Best hotel in india")
# print(res)


res = search_flights("Plan 7 day Nepal trip from bangladesh")
print(res)