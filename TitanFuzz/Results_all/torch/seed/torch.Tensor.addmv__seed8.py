mat = torch.randn(4, 3, requires_grad=True)
vec = torch.randn(3, requires_grad=True)
torch.Tensor.addmv_(mat, vec, beta=1, alpha=1)