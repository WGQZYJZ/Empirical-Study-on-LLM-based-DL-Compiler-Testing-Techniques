input_tensor = torch.tensor([1, 2, 3, 4, 5])
other = torch.tensor([5, 4, 3, 2, 1])
result = torch.Tensor.lt_(input_tensor, other)