input = torch.randint(0, 10, (5,))
combinations = torch.combinations(input, r=2, with_replacement=False)