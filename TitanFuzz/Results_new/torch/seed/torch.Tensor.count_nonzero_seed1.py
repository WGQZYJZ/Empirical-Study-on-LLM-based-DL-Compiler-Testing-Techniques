_input_tensor = torch.randint(0, 2, (2, 3, 3, 3))
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)