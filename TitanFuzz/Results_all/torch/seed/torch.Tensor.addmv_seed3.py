input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 3)
vec = torch.randn(3)
result = torch.Tensor.addmv(input_tensor, mat, vec)