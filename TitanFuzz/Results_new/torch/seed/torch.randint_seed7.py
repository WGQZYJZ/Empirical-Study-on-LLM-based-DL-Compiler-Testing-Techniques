input_data = torch.randint(low=0, high=10, size=(5, 5))
output_data = torch.randint_like(input_data, low=0, high=10)
output_data = torch.randint_like(input_data, low=0, high=10, dtype=torch.float)