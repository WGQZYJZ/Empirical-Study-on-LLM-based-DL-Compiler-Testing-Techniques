input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.cumprod_(input_tensor, dim=1)