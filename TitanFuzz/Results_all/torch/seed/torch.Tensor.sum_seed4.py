_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=1, keepdim=False, dtype=None)