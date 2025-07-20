input_data = torch.randn(1, 2, 3, 4)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input_data)