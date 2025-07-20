input_tensor = torch.rand(3, 4)
other = torch.rand(3, 4)
result = torch.Tensor.less_equal_(input_tensor, other)