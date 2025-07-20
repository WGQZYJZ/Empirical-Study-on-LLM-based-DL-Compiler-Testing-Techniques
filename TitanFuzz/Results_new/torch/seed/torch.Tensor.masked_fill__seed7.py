input_tensor = torch.randn(2, 3)
mask = torch.tensor([[0, 1, 0], [1, 0, 1]])
value = torch.tensor(0.5)
output_tensor = torch.Tensor.masked_fill_(input_tensor, mask, value)