from google_takeout_parser.merge import merge_events, TakeoutParser
itrs = []  # list of iterators of google events
takeout_path = "/Users/miguelhabana/Desktop/google-takeout/"
takeout_folders = ["Takeout", "Takeout 2", "Takeout 3", "Takeout 4", "Takeout 5"] 
for path in takeout_folders:
    # ignore errors, error_policy can be 'yield', 'raise' or 'drop'
    tk = TakeoutParser(takeout_path+path, error_policy="drop")
    itrs.append(tk.parse(cache=False))
res = list(merge_events(*itrs))


# from google_takeout_parser.path_dispatch import TakeoutParser
# from google_takeout_parser.models import Activity

# takeout_path = "/Users/miguelhabana/Desktop/google-takeout/"
# activity = list(
#     TakeoutParser(takeout_path + "Takeout", error_policy="raise").parse(
#         cache=False, filter_type=Activity
#     )
# )