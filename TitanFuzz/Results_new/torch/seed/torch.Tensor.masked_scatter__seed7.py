input_tensor = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0]])
source = torch.FloatTensor([3, 4, 5, 6])
torch.Tensor.masked_scatter_(input_tensor, mask, source)