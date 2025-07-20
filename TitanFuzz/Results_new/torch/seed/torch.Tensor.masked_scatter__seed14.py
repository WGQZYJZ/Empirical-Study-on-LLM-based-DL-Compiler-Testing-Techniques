input_tensor = torch.randn(2, 3, 4)
mask = torch.ByteTensor([[0, 1, 1], [1, 0, 0]])
source = torch.ones(2, 3)
torch.Tensor.masked_scatter_(input_tensor, mask, source)