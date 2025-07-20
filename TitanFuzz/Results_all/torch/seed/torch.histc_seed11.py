input_data = torch.randn(1000)
hist_data = torch.histc(input_data, bins=100, min=0, max=0)