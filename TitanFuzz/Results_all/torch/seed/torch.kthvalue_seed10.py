data = torch.randn(3, 5)
k = 2
(values, indices) = torch.kthvalue(data, k, dim=1)