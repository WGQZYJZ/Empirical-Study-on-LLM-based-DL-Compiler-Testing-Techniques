input_tensor = torch.randn(4, 3)
mat = torch.randn(3, 3)
vec = torch.randn(3)
out = torch.Tensor.addmv(input_tensor, mat, vec)