_input_tensor = torch.rand(2, 3, 4)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)