input_data = torch.arange((- 2), 3, dtype=torch.float)
output_data = torch.clamp(input_data, min=(- 1), max=1)
output_data = torch.clamp_min(input_data, min=(- 1))
output_data = torch.clamp_max(input_data, max=1)