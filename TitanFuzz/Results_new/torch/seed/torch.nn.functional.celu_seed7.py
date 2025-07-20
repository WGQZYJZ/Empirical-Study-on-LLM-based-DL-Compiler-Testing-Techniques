input = torch.randn(1, 1, 3, 3)
torch.nn.functional.celu(input, alpha=1.0, inplace=False)