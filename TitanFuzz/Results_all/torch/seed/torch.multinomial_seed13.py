input = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
output = torch.multinomial(input, 3, replacement=False)