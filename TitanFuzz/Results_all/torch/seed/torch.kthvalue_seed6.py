input = torch.randn(3, 4)
k = 3
torch.kthvalue(input, k, dim=1)