input_tensor = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
unflatten = torch.nn.Unflatten(dim=1, unflattened_size=(3, 4))
unflatten(input_tensor)