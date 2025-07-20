input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
result = torch.Tensor.less_(input_tensor, other)