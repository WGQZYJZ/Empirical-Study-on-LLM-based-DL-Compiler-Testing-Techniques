input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.cumprod_(input_tensor, dim=1, dtype=None)