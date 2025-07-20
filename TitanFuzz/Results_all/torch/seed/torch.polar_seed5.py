abs_data = torch.randn(2, 3, 4)
angle_data = torch.randn(2, 3, 4)
output = torch.polar(abs_data, angle_data)