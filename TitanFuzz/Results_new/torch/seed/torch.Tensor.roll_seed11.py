_input_tensor = torch.randn(2, 3)
_shifts = [1, 2]
_dims = [0, 1]
_output_tensor = torch.Tensor.roll(_input_tensor, _shifts, _dims)