input_data = torch.randn(3, 4)
cumsum_data = torch.cumsum(input_data, dim=0)
cumsum_data = torch.cumsum(input_data, dim=1)