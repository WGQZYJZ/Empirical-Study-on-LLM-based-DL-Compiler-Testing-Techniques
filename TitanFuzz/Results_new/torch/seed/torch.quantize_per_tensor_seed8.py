a = torch.randn(1, 1, 3, 3)
a = torch.randn(1, 1, 3, 3)
a_quant = torch.quantize_per_tensor(a, scale=0.5, zero_point=2, dtype=torch.quint8)