input_data = torch.randn(5, 3)
output = torch.nn.functional.leaky_relu(input_data)