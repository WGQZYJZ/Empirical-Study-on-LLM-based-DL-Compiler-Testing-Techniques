input_data = torch.randint(low=0, high=10, size=(10,))
output = torch.combinations(input_data, r=2, with_replacement=False)