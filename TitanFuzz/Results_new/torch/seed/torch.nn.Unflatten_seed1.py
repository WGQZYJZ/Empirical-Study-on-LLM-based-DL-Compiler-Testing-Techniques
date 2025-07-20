input_data = torch.rand(1, 1, 4, 4)
unflatten = torch.nn.Unflatten(2, (2, 2))