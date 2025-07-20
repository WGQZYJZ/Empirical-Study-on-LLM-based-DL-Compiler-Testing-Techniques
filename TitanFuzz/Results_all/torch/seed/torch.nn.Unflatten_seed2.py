input_data = torch.tensor([[1, 2, 3, 4, 5, 6]])
unflatten = torch.nn.Unflatten(1, (2, 3))
output = unflatten(input_data)