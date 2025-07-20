input_data = torch.randn(10, 10)
output = torch.diag(input_data)
output = torch.diag_embed(input_data)
output = torch.diagflat(input_data)