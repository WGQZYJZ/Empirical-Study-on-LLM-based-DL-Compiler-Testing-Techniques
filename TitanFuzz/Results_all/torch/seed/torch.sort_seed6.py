input_data = torch.rand(4, 3)
(sorted_data, sorted_indices) = torch.sort(input_data)
(sorted_data, sorted_indices) = torch.sort(input_data, dim=1)
(sorted_data, sorted_indices) = torch.sort(input_data, dim=1, descending=True)
(sorted_data, sorted)