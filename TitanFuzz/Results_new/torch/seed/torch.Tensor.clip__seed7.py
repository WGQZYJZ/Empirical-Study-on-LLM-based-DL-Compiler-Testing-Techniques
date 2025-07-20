input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.clip_(input_tensor, min=(- 1), max=1)