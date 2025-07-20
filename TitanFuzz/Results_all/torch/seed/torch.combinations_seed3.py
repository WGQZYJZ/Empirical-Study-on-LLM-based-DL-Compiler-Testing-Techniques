input = torch.tensor([1, 2, 3, 4, 5])
combinations = torch.combinations(input, r=2, with_replacement=False)
combinations = torch.combinations(input, r=3, with_replacement=False)