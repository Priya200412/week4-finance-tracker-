def safe_input(msg):
    try:
        return input(msg)
    except KeyboardInterrupt:
        print("\nCancelled")
        return ""
