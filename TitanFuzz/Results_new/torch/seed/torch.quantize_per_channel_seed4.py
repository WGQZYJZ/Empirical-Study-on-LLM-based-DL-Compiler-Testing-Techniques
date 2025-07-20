input = torch.randn(2, 3, 4, 5)
output = torch.quantize_per_channel(input, scales=torch.tensor([1.0, 2.0, 3.0]), zero_points=torch.tensor([0, 0, 0]), axis=1, dtype=torch.quint8)