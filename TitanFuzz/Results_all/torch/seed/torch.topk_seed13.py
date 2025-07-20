a = torch.randn(5, 3)
(values, indices) = torch.topk(a, 2)
(values, indices) = torch.topk(a, 2, dim=1)