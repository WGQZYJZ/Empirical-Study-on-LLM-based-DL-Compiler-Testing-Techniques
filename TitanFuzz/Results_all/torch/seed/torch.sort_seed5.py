data = torch.randn(2, 3, 4)
(sorted_data, sorted_indices) = torch.sort(data)
(sorted_data, sorted_indices) = torch.sort(data, dim=1)
(sorted_data, sorted_indices) = torch.sort(data, dim=2)