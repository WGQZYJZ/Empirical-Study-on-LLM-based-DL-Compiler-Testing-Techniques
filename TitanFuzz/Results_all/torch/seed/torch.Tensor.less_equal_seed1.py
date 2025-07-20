input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
output = torch.Tensor.less_equal(input_tensor, other)