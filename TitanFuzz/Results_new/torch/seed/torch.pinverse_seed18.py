input = torch.randn(2, 3)
torch.pinverse(input, rcond=1e-15)