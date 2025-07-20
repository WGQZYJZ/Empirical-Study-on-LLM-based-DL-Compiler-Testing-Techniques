input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
pad = (1, 1, 2, 2)
output = torch.nn.functional.pad(input, pad, mode='constant', value=0)