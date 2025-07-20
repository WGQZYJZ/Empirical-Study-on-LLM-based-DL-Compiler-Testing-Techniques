input = torch.randn(1, 1, 5, 5)
output = torch.nn.Upsample(size=(9, 9), mode='nearest')(input)