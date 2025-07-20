input_data = torch.randint(0, 10, (4, 4))
sort_indices = torch.argsort(input_data, dim=(- 1), descending=False)
sorted_data = torch.sort(input_data, dim=(- 1), descending=False)
(top3_data, top3_indices) = torch.topk(input_data, 3, dim=(- 1), largest=True)