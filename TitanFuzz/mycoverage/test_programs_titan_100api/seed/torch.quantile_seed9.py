input = torch.randn(3, 4, 5)
q = torch.tensor([0.25, 0.5, 0.75])
torch.quantile(input, q, dim=None, keepdim=False, out=None)