input = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
pad = (1, 1, 1, 1)
output = torch.nn.functional.pad(input, pad, mode='constant', value=0)