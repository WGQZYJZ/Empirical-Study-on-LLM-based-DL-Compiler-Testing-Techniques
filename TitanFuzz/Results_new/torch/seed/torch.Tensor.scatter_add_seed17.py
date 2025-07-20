input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
dim = 0
index = torch.tensor([0, 1])
src = torch.tensor([[10, 11, 12], [13, 14, 15]])
torch.Tensor.scatter_add(input_tensor, dim, index, src)