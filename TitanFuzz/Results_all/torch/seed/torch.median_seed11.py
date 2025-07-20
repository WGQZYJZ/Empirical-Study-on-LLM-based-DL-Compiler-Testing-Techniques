input_data = torch.randn(2, 3, 3)
output = torch.median(input_data)
output = torch.median(input_data, dim=1)