input_data = torch.randn(1000)
result = torch.histc(input_data, bins=100, min=0, max=0)