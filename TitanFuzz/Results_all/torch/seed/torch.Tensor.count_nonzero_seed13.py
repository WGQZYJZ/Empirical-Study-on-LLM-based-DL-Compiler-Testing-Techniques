_input_tensor = torch.randn(1, 3, 3, requires_grad=True)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)