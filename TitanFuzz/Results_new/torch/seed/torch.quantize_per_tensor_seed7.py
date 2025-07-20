X = torch.rand(3, 3).float()
X_quant = torch.quantize_per_tensor(X, scale=0.5, zero_point=5, dtype=torch.quint8)
X_dequant = X_quant.dequantize()