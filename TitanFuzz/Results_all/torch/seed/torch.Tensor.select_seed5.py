input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.Tensor.select(input_tensor, 0, 1)