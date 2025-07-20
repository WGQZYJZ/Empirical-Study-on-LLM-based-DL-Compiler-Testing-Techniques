input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output = torch.nn.functional.pad(input, (1, 1, 1, 1), mode='constant', value=0)