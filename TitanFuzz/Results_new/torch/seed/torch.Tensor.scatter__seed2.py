input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = torch.tensor([[0, 1, 2], [0, 1, 2]])
src = torch.tensor([[1, 1, 1], [2, 2, 2]])
output_tensor = torch.Tensor.scatter_(input_tensor, 0, index, src)