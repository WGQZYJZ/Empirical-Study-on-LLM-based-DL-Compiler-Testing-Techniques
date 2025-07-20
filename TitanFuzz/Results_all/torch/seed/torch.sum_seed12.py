input = torch.rand(2, 3, 4)
output = torch.sum(input, dim=1, keepdim=True)