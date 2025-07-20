input_tensor = torch.randn(2, 3)
result = torch.Tensor.log_normal_(input_tensor, mean=1, std=2)