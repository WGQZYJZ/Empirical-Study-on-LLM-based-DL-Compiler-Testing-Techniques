input_data = torch.randn(3, 4)
sorted_indices = torch.argsort(input_data, dim=(- 1), descending=True)
sorted_data = torch.gather(input_data, dim=(- 1), index=sorted_indices)