input_data = torch.randn(2, 3, 4)
cummin_result = torch.cummin(input_data, dim=1)
cummin_result = torch.cummin(input_data, dim=2)
cummin_result = torch.cummin(input_data, dim=0)