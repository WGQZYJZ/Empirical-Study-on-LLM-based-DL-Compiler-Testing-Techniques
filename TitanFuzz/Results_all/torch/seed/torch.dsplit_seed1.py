input = torch.randn(2, 3, 4, 5)
torch.dsplit(input, 2)
torch.dsplit(input, [1, 2])
torch.dsplit(input, [2, 3])