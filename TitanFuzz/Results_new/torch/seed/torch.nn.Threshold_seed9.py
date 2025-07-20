input = torch.randn(1, 1, 3, 3)
threshold = torch.nn.Threshold(0.5, 0.5)
output = threshold(input)