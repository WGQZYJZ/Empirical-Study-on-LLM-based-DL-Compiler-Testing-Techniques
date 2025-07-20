input_tensor = torch.randn(5, 3)
mat = torch.randn(3, 5)
vec = torch.randn(5)
out = torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)