input_tensor = torch.rand(1, 2, 3, 4)
is_quantized = torch.Tensor.is_quantized(input_tensor)