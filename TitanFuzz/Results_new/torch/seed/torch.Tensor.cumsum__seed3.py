input_tensor = torch.randn(3, 4)
output_tensor = torch.Tensor.cumsum_(input_tensor, dim=0, dtype=None)