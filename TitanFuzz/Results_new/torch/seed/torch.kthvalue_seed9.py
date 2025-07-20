input = torch.rand(3, 5)
(kth_value, index) = torch.kthvalue(input, 2, dim=1, keepdim=False)