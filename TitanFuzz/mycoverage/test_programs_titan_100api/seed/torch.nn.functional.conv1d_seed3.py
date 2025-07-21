input_data = torch.randn(1, 1, 4)
weight_data = torch.randn(1, 1, 3)
output = torch.nn.functional.conv1d(input_data, weight_data)