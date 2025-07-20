input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([0, 2])
src = torch.tensor([[10, 11, 12], [13, 14, 15]])
torch.Tensor.scatter_add(input_tensor, 0, index, src)