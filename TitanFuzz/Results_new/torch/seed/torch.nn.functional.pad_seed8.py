input = torch.randn(2, 3, 3)
pad = (1, 2, 3, 4)
output = torch.nn.functional.pad(input, pad, mode='constant', value=0)