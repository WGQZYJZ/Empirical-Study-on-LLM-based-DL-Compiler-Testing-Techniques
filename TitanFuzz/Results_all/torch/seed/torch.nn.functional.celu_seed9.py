input = torch.randn(4, 4)
torch.nn.functional.celu(input, alpha=1.0, inplace=False)
torch.nn.functional.celu(input, alpha=0.5, inplace=False)
torch.nn.functional.celu(input, alpha=0.1, inplace=False)
torch.nn.functional.celu(input, alpha=0.01, inplace=False)
torch.nn.functional.celu(input, alpha=0.001, inplace=False)
torch.nn.functional.celu(input, alpha=0.0001, inplace=False)