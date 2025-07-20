input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1, 1], [1, 2, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.scatter_add(input_tensor, dim=0, index=index, src=src)