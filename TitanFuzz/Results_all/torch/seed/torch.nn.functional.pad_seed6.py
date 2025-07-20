input = torch.randn(3, 3, 3)
output = torch.nn.functional.pad(input, (1, 1, 1, 1), mode='constant', value=0)