input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.clip(input_tensor, min=(- 0.5), max=0.5)