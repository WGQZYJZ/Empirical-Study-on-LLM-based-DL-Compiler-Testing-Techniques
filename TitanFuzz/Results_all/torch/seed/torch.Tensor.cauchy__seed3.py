input_tensor = torch.rand(10)
output_tensor = torch.Tensor.cauchy_(input_tensor, median=1, sigma=2)