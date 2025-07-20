input_tensor = torch.randn(4, 3, 5)
dim = 1
index = torch.tensor([0, 1, 2, 1])
src = torch.randn(4, 5)
torch.Tensor.scatter_add_(input_tensor, dim, index, src)