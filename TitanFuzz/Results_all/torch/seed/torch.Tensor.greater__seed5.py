_input_tensor = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
_output_tensor = torch.Tensor.greater_(_input_tensor, 5)
_output_tensor = _input_tensor.gt_(5)