input = torch.randn(1, 2, 3, dtype=torch.float32)
quantized_input = torch.quantize_per_tensor(input, scale=1.0, zero_point=0, dtype=torch.quint8)
input = torch.randn(1, 2, 3, dtype=torch.float32)