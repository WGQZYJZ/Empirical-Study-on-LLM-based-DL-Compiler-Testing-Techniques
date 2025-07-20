input = torch.randn(1, 3, 224, 224)
input = input.float()
quantized_input = torch.quantize_per_tensor(input, scale=0.1, zero_point=5, dtype=torch.quint8)