_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=1, keepdim=False, dtype=None)