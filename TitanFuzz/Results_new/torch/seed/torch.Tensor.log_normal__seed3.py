input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.log_normal_(input_tensor, mean=1, std=2, generator=None)