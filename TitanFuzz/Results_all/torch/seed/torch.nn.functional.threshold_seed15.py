input = torch.randn(1, 3, 3, 3)
output = torch.nn.functional.threshold(input, 0.5, 0)