_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.fill_diagonal_(_input_tensor, 1, wrap=False)