_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
_output_tensor = torch.Tensor.maximum(_input_tensor, other)