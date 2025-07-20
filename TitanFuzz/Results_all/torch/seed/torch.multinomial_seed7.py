input = torch.Tensor([[0.2, 0.3, 0.5]])
output = torch.multinomial(input, 3, replacement=False)
output = torch.multinomial(input, 3, replacement=True)