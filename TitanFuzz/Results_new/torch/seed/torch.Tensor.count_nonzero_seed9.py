_input_tensor = torch.Tensor([[0, 0, 1, 1], [0, 1, 1, 0]])
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)