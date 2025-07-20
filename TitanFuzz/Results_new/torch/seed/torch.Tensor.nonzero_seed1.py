_input_tensor = torch.Tensor([[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1]])
_output_tensor = torch.Tensor.nonzero(_input_tensor, as_tuple=False)