input_tensor = torch.rand(2, 3)
mat = torch.rand(3, 2)
vec = torch.rand(2)
torch.Tensor.addmv_(input_tensor, mat, vec, beta=1, alpha=1)