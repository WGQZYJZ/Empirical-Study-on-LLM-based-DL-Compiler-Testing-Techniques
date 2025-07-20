_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.narrow_copy(_input_tensor, 1, 0, 2)