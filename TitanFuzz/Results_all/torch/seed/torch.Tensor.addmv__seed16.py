mat = torch.randn(4, 3, dtype=torch.float)
vec = torch.randn(3, dtype=torch.float)
torch.Tensor.addmv_(mat, vec, beta=1, alpha=1)