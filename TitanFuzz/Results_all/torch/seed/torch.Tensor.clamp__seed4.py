input_tensor = torch.randn(5)
output_tensor = torch.Tensor.clamp_(input_tensor, min=(- 0.5), max=0.5)