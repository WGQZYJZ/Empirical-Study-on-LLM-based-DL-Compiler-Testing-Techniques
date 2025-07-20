_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.as_subclass(_input_tensor, torch.Tensor)