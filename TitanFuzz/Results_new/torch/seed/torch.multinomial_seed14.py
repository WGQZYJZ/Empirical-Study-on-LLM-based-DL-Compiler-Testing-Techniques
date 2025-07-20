input = torch.FloatTensor([[0.1, 0.2, 0.3, 0.4, 0.5], [0.1, 0.2, 0.3, 0.4, 0.5]])
result = torch.multinomial(input, 3, replacement=False)
result = torch.multinomial(input, 3, replacement=True)
result = torch.multinomial(input, 3, replacement=True, out=torch.LongTensor([0, 0, 0]))