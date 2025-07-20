input = torch.randn(2, 3, 4)
output1 = torch.dsplit(input, 2)
output2 = torch.dsplit(input, [1, 2])