if __name__ != "__main__":
    import hidden_4

    args = dir(hidden_4)
    for name in args:
        if name[:2] != "__":
            print("{}".format(name))