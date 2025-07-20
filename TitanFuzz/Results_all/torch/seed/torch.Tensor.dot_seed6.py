_input_tensor = torch.rand(1, 3)
other = torch.rand(3, 1)
_output_tensor = torch.Tensor.dot(_input_tensor, other)