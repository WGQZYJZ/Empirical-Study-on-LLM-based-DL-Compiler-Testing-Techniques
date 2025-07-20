input_data = torch.randn(5, 3)
cumsum_output = torch.cumsum(input_data, dim=1)
cumsum_output = torch.cumsum(input_data, dim=0)