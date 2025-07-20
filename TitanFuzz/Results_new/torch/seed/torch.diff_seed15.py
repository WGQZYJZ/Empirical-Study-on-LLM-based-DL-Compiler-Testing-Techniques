input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
output_data = torch.diff(input_data, n=1, dim=(- 1))
output_data = torch.diff(input_data, n=1, dim=(- 1), prepend=torch.tensor([0], dtype=torch.float32), append=torch.tensor([0], dtype=torch.float32))