input_tensor = torch.rand(10, 10)
mask = torch.rand(10, 10)
value = torch.rand(1)
torch.Tensor.masked_fill_(input_tensor, mask, value)