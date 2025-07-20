input_tensor = torch.rand(2, 3)
mat = torch.rand(3, 4)
vec = torch.rand(4)
output_tensor = torch.Tensor.addmv(input_tensor, mat, vec)