input = torch.randn(3, 3)
result = torch.triu(input)
result = torch.triu(input, diagonal=1)
result = torch.triu(input, diagonal=(- 1))