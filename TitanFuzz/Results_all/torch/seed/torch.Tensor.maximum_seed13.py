_input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
_output_tensor = torch.Tensor.maximum(_input_tensor, other)