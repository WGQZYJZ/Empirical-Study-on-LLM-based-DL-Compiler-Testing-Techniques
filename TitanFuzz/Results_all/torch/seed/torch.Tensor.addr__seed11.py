vec1 = torch.rand(4, 4)
vec2 = torch.rand(4, 4)
torch.Tensor.addr_(vec1, vec2, beta=1, alpha=1)