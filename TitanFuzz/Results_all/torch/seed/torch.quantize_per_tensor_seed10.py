X = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0], dtype=torch.float)
qX = torch.quantize_per_tensor(X, scale=0.5, zero_point=2, dtype=torch.quint8)
dqX = qX.dequantize