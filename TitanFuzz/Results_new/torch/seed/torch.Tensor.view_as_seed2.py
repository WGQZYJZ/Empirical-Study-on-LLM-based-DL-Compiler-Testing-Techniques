_input_tensor = torch.randn(2, 3)
_other = torch.randn(3, 2)
_output_tensor = torch.Tensor.view_as(_input_tensor, _other)