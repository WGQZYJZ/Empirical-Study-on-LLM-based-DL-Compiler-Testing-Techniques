input_data = torch.randn(2, 3, 4)
median_output = torch.median(input_data, dim=1, keepdim=False)