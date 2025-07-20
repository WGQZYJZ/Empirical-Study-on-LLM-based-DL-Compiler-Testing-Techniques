input_data = torch.rand(1, 3, 1, 1)
broadcast_data = torch.broadcast_to(input_data, (3, 3, 3, 3))