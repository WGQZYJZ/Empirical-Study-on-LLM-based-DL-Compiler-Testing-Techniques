input = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 0.9, 0.9, 0.9]])
torch.multinomial(input, 3)
torch.multinomial(input, 3, replacement=True)
torch.multinomial(input, 3, replacement=False)
out = torch.LongTensor(3, 3)
torch.multinomial(input, 3, out=out)
out
gen = torch.Generator()
torch.multinomial(input, 3, generator=gen)