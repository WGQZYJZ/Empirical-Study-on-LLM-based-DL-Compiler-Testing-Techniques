input_tensor = torch.rand(5, 3)
mat = torch.rand(3, 4)
vec = torch.rand(4)
torch.Tensor.addmv_(input_tensor, mat, vec)