input_data = torch.rand(2, 3)
quantized_data = torch.quantize_per_tensor(input_data, scale=1.0, zero_point=0, dtype=torch.quint8)