input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.cauchy_(input_tensor, median=0, sigma=1)