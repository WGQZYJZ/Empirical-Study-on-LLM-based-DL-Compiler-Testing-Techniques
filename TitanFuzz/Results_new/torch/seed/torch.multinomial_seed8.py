input = torch.Tensor([[0.1, 0.2, 0.3, 0.4, 0.5], [0.1, 0.2, 0.3, 0.4, 0.5]])
output = torch.multinomial(input, 3, replacement=True)