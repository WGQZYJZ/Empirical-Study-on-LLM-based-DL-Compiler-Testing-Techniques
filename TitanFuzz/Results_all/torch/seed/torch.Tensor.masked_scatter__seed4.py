input_data = torch.randn(3, 4)
mask = torch.ByteTensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
source = torch.randn(3, 4)
torch.Tensor.masked_scatter_(input_data, mask, source)