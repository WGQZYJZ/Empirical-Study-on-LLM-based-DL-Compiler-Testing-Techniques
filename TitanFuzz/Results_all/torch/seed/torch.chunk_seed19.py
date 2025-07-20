input = torch.randn(4, 4)
output1 = torch.chunk(input, 2, dim=0)
output2 = torch.chunk(input, 2, dim=1)