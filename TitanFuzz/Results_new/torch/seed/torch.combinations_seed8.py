input_data = torch.arange(1, 7)
combinations = torch.combinations(input_data, r=2, with_replacement=False)
combinations = combinations.numpy()