input_data = torch.arange(1, 6, dtype=torch.float)
output_data = torch.logcumsumexp(input_data, dim=0)
output_data = torch.logcumsumexp(input_data, dim=0, out=input_data)