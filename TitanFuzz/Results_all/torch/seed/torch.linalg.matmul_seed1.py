input = torch.randn(2, 3)
other = torch.randn(3, 4)
output = torch.linalg.matmul(input, other)
output = torch.empty(2, 4)
torch.linalg.matmul(input, other, out=output)