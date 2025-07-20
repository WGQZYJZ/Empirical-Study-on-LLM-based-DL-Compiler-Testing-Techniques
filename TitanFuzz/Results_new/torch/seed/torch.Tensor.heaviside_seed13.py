_input_tensor = torch.randn(5, 5)
_output_tensor = torch.Tensor.heaviside(_input_tensor, 0)