_input_tensor = torch.randn(1, 2, 3, 4, 5)
_output_tensor = torch.Tensor.resolve_neg(_input_tensor)