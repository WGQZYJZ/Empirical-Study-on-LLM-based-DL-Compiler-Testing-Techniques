input_tensor = torch.randn(5, 3)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 0.5), max=0.5)