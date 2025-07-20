input = torch.randn(1, 3, 224, 224)
scales = torch.tensor([1.0, 1.0, 1.0])
zero_points = torch.tensor([0, 0, 0])
axis = 1
dtype = torch.quint8
output = torch.quantize_per_channel(input, scales, zero_points, axis, dtype)
input = torch.randn(1, 3, 224, 224)