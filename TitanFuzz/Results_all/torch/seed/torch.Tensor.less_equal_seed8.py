input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
other = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
output = torch.Tensor.less_equal(input_tensor, other)