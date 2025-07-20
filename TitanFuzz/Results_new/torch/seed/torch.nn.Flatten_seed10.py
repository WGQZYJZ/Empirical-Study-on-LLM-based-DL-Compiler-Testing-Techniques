input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))