input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
output_tensor = torch.Tensor.less_equal_(input_tensor, other)