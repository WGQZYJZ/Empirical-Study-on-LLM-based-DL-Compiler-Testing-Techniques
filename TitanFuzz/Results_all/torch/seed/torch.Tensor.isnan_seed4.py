_input_tensor = torch.randn(2, 3, requires_grad=True)
_output_tensor = torch.Tensor.isnan(_input_tensor)