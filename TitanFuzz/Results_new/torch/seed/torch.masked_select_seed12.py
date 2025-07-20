input = torch.randn(3, 4)
input
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
mask
torch.masked_select(input, mask)
input = torch.randn(3, 4)
input
mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]])
mask
out = torch.masked_select(input, mask)
out
input = torch.randn(3, 4)
input