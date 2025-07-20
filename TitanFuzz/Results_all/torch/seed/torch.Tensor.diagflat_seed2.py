_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.diagflat(_input_tensor, offset=0)