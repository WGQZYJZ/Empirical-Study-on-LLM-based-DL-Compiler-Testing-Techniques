input_data = torch.rand(1, 3, 224, 224)
quantized_data = torch.quantize_per_tensor(input_data, 0.01, 0, torch.quint8)
input_data = torch.rand(1, 3, 224, 224)