input_data = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.uint8)
output_data = torch.dequantize(input_data)
quantized_tensor = torch.quantize_per_tensor(output_data, scale=1.0, zero_point=0, dtype=torch.quint8)