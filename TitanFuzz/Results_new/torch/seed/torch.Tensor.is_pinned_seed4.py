_input_tensor = torch.randn(1, 2, 3, 4)
_output_tensor = torch.Tensor.is_pinned(_input_tensor)