input = torch.randn(2, 3)
torch.std(input)
input = torch.randn(2, 3)
torch.std(input, dim=0, unbiased=False)