input = torch.randn(3, 4)
sort_index = torch.argsort(input, dim=(- 1), descending=False)
sort_data = torch.gather(input, dim=(- 1), index=sort_index)