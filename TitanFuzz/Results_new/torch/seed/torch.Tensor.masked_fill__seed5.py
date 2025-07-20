input_tensor = torch.ones(3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 1], [1, 1, 1]])
value = 3
torch.Tensor.masked_fill_(input_tensor, mask, value)