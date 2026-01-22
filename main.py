from search import search_records

print("🏥 Medical Record Retrieval Assistant")
print("Type 'exit' to quit.\n")

while True:
    query = input("Enter medical query: ")

    if query.lower() == "exit":
        break

    results = search_records(query)

    print("\n🔍 Retrieved Patient History:")
    if not results:
        print("No relevant records found.")
    else:
        for i, res in enumerate(results, 1):
            print(f"\nResult {i}:\n{res}")

    print("\n" + "-" * 50)
