input = torch.randn(3, 4)
(kthvalue, index) = torch.kthvalue(input, 2, dim=1, keepdim=True)