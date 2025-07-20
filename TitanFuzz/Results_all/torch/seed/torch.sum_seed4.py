input = torch.randn(4, 3)
sum_result = torch.sum(input, dim=1)
sum_result = torch.sum(input, dim=1, keepdim=True)
sum_result = torch.sum(input, dim=1, keepdim=False)