input_tensor = torch.randn(1, 2, 3, 4, dtype=torch.float32)
output_tensor = torch.Tensor.is_quantized(input_tensor)