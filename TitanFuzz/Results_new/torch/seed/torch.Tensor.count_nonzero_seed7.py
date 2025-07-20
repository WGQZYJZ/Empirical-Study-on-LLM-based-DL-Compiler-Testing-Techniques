_input_tensor = torch.tensor([[0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=0)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=1)