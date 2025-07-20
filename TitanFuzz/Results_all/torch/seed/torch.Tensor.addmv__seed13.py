input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 2)
vec = torch.randn(2)
torch.Tensor.addmv_(input_tensor, mat, vec, alpha=0.5, beta=2.0)