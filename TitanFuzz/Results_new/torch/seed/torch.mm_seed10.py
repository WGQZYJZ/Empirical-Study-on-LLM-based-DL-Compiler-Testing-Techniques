input = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
output = torch.mm(input, mat2)
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
output = torch.bmm(batch1, batch2)