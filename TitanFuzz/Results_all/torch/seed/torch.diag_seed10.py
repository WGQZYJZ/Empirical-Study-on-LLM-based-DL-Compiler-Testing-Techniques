input_data = torch.arange(1, 10)
output_data = torch.diag(input_data)
output_data = torch.diag(input_data, diagonal=1)
output_data = torch.diag(input_data, diagonal=(- 1))