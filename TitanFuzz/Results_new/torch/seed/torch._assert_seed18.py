a = torch.rand(5, 3)
b = torch.rand(3, 4)
torch._assert((a.shape[1] == b.shape[0]), 'The column of a must be the same as the row of b')
c = torch.matmul(a, b)