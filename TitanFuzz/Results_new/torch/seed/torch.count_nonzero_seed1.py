input_data = torch.randn(3, 4)
count_nonzero = torch.count_nonzero(input_data)
count_nonzero = torch.count_nonzero(input_data, dim=0)
count_nonzero = torch.count_nonzero(input_data, dim=1)