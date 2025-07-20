input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
output = torch.pinverse(input, rcond=1e-15)