_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.cumprod_(_input_tensor, dim=1)