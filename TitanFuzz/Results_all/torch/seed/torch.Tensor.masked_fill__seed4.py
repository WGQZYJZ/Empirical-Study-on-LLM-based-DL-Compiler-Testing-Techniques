input_tensor = torch.randn(3, 4)
mask = torch.randint(0, 2, (3, 4), dtype=torch.bool)
value = torch.rand(1)
torch.Tensor.masked_fill_(input_tensor, mask, value)