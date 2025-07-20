input_tensor = torch.randn(4, 4)
index = torch.tensor([[0, 1, 2, 3], [0, 1, 2, 3]])
src = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
torch.Tensor.scatter_add_(input_tensor, 1, index, src)
input_tensor = torch.randn(4, 4)
index