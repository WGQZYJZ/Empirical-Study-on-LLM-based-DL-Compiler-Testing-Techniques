input_tensor = torch.randn(1, 3, 224, 224, dtype=torch.float32)
half_input_tensor = torch.Tensor.half(input_tensor)