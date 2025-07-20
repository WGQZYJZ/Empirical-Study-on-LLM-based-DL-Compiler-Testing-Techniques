input_tensor = torch.rand(3, 5)
index = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 3]])
src = torch.tensor([[1, 0, 1, 2], [4, 1, 2, 3]])
output = torch.Tensor.scatter_add_(input_tensor, 1, index, src)