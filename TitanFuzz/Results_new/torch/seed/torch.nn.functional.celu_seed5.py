input = torch.randn(2, 3)
output = torch.nn.functional.celu(input, alpha=1.0, inplace=False)