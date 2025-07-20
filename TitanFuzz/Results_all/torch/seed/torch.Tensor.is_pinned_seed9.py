_input_tensor = torch.randn(10, 20, 30)
_output_tensor = torch.Tensor.is_pinned(_input_tensor)