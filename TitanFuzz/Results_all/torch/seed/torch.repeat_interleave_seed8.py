input_data = torch.arange(6).view(2, 3)
output_data = torch.repeat_interleave(input_data, repeats=2, dim=0)
output_data = torch.repeat_interleave(input_data, repeats=2, dim=1)
output_data = torch.repeat_interleave(input_data, repeats=2)