input = torch.randn(4, 4)
output = torch.nn.Threshold(0.5, 0.5)(input)