mat = torch.rand(3, 4)
vec = torch.rand(4)
torch.Tensor.addmv_(mat, vec, beta=1, alpha=1)