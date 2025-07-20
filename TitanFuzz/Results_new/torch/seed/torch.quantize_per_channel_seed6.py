input_data = torch.randn(2, 3, 4, 5, dtype=torch.float)
input_data = torch.randn(2, 3, 4, 5, dtype=torch.float)
output = torch.quantize_per_channel(input_data, scales=torch.tensor([0.1, 0.2, 0.3]), zero_points=torch.tensor([3, 4, 5]), axis=1, dtype=torch.quint8)
output = torch.quantize_per_tensor(input_data, 0.1, 3, dtype=torch.quint8)