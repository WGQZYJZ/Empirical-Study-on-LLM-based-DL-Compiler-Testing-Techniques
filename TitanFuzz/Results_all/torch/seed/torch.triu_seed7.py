input = torch.randn(3, 3)
output = torch.triu(input)
output = torch.triu(input, diagonal=1)
output = torch.triu(input, diagonal=1, out=torch.empty(3, 3))