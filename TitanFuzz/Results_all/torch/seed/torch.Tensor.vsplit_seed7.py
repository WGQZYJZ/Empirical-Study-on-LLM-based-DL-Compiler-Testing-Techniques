_input_tensor = torch.Tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
_output_tensor = torch.Tensor.vsplit(_input_tensor, 2)