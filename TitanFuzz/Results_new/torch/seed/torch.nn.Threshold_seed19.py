input = torch.randn(1, 1, 3, 3)
output = torch.nn.Threshold(0.5, 0.0)(input)