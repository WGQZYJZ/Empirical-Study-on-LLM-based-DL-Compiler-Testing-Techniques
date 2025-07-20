input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 2, 0], [0, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.scatter(input_tensor, 0, index, src)