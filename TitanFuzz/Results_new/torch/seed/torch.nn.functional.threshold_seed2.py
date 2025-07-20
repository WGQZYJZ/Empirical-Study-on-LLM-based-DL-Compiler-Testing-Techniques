input = torch.randn(3, 3)
output = torch.nn.functional.threshold(input, threshold=0.5, value=0.0)