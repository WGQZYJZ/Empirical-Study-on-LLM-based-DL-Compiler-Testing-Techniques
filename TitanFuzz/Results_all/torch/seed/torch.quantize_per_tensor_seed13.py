input_data = np.random.randn(100, 100)
input_data = input_data.astype(np.float32)
input_tensor = torch.tensor(input_data)
quantized_tensor = torch.quantize_per_tensor(input_tensor, scale=1.0, zero_point=0, dtype=torch.quint8)