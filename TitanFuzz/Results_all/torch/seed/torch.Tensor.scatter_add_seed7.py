input_tensor = torch.ones(3, 3)
index = torch.tensor([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
src = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
result = torch.Tensor.scatter_add(input_tensor, dim=1, index=index, src=src)