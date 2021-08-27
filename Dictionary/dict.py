

sal_info = {"austin":57875, "Boston":58778}
print(sal_info)

sal_info["Boston"]=587876
print("Boston Edited: ", sal_info)

sal_info["Atlanta"] = 528758
print("Added Atlanta: ", sal_info)

del sal_info["austin"]
print("Deleted Austin: ", sal_info)

sal_info.clear()
print("Clear: ", sal_info)


