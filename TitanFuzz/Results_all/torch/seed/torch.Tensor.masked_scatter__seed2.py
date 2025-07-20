input_tensor = torch.rand(3, 3)
mask = torch.tensor([[1, 0, 1], [1, 1, 0], [0, 0, 1]], dtype=torch.uint8)
source = torch.rand(3, 3)
torch.Tensor.masked_scatter_(input_tensor, mask, source)