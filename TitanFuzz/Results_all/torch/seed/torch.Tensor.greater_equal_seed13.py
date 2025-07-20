_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.greater_equal(_input_tensor, 0)
_output_tensor = torch.ge(_input_tensor, 0)