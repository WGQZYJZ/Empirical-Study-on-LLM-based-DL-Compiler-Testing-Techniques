input_tensor = torch.rand(5, 3)
dim = 0
index = torch.tensor([1, 2, 3, 0, 4])
src = torch.rand(5, 3)
output_tensor = torch.Tensor.scatter_add(input_tensor, dim, index, src)