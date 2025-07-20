input_data = torch.randn(1, 2, 3, 4)
flattened_input = torch.nn.Flatten(start_dim=1, end_dim=(- 1))(input_data)