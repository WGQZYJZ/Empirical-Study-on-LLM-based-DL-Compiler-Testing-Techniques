input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
output_tensor = torch.Tensor.less_(input_tensor, other)