input_data = torch.randn(10, 5)
output = torch.nn.functional.layer_norm(input_data, [5])