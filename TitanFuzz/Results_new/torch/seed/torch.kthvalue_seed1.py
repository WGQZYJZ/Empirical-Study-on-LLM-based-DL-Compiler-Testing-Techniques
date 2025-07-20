input = torch.randn(3, 4)
k = 2
(out, index) = torch.kthvalue(input, k, dim=1, keepdim=True)