input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
other = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
result = torch.Tensor.dot(input_tensor, other)