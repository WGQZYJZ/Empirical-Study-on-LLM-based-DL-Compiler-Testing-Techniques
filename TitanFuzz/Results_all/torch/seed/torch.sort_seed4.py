x = torch.randn(1, 4)
(sorted, indices) = torch.sort(x, dim=1)
(sorted, indices) = torch.sort(x, dim=0)
(sorted, indices) = torch.sort(x, dim=1, descending=True)