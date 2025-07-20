tensors = torch.quantize_per_tensor(torch.randn(5, 5).float(), scale=0.5, zero_point=5, dtype=torch.quint8)
torch.dequantize(tensors)