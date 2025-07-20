input = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [8, 7, 6, 5]])
(topk_values, topk_indices) = torch.topk(input, k=2, dim=1)