input_data = torch.randn(2, 1, 2, 1, 2)
output = torch.squeeze(input_data)
output = torch.squeeze(input_data, dim=0)
output = torch.squeeze(input_data, dim=1)
output = torch.squeeze(input_data, dim=2)
output = torch.squeeze(input_data, dim=3)
output = torch.squeeze(input_data, dim=4)
output = torch.squeeze(input_data, dim=(- 1))
output = torch.squeeze