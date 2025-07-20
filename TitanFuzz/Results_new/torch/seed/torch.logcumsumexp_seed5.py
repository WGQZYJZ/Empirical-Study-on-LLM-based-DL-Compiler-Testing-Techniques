input_data = torch.randn(5, 3)
output_data = torch.logcumsumexp(input_data, dim=1)