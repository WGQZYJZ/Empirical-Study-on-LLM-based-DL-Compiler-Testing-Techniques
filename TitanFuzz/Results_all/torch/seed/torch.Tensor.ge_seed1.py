input_tensor = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
other = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
result = torch.Tensor.ge(input_tensor, other)