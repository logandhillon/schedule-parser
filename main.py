def main() -> None:
    schedule = ""

    print("Please paste your schedule below. When the entire schedule is pasted, type 'DONE'.")
    while True:
        s = input()
        if (s == "DONE"):
            break
        else:
            schedule += s + '\n'

    print(schedule)
    print("EXECUTION COMPLETE")


if __name__ == "__main__": main()