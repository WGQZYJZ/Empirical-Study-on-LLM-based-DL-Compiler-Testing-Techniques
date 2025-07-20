input = torch.Tensor([[0.3, 0.2, 0.5], [0.1, 0.2, 0.7]])
output = torch.multinomial(input, 2, replacement=False)
output = torch.multinomial(input, 2, replacement=True)