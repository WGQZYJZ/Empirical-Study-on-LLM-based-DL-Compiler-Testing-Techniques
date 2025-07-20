input_tensor = torch.randn(4, 3)
mat = torch.randn(3, 5)
vec = torch.randn(5)
result = torch.Tensor.addmv(input_tensor, mat, vec, beta=1, alpha=1)