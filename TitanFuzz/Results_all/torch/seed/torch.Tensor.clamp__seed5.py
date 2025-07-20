_input_tensor = torch.randn(10)
_clamped_tensor = torch.Tensor.clamp_(_input_tensor, min=(- 0.5), max=0.5)