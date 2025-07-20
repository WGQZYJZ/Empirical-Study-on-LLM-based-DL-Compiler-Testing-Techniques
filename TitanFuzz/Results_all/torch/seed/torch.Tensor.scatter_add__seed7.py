input_tensor = torch.rand(2, 3)
dim = 1
index = torch.tensor([0, 1, 1], dtype=torch.long)
src = torch.tensor([1, 2, 3], dtype=torch.float)
torch.Tensor.scatter_add_(input_tensor, dim, index, src)