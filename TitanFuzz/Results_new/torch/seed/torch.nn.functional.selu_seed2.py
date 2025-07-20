input_data = torch.randn(1, 3)
output = torch.nn.functional.selu(input_data)
output = torch.selu(input_data)