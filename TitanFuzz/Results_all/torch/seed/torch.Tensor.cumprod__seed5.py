input_tensor = torch.arange(1, 10).view(3, 3)
output_tensor = torch.Tensor.cumprod_(input_tensor, dim=1)