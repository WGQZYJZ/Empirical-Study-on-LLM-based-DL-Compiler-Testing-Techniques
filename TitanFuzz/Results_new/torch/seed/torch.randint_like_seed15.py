input_data = torch.randn(10, 10)
output_data = torch.randint_like(input_data, low=0, high=10, dtype=torch.int32)