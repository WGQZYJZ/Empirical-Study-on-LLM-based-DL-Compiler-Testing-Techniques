_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.copy_(_input_tensor, src=torch.randn(2, 3))