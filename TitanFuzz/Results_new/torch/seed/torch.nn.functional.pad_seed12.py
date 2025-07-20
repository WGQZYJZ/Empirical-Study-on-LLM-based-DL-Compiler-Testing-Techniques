input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
padded_data = torch.nn.functional.pad(input_data, (1, 1, 2, 2), mode='constant', value=0)