input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.tensor(input_data)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input_data)