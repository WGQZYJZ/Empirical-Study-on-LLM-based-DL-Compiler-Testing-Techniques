input_data = torch.randn(2, 3)
k = 2
(values, indices) = torch.topk(input_data, k)
(values, indices) = torch.topk(input_data, k, dim=1)
(values, indices) = torch.topk(input_data, k, dim=1, largest=False)