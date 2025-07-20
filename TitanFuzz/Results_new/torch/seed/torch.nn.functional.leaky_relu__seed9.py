input_data = torch.rand(3, 3)
output = torch.nn.functional.leaky_relu_(input_data)