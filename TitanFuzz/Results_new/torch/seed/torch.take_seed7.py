input = torch.randn(4, 4)
index = torch.tensor([1, 2])
torch.take(input, index)
input = torch.randn(4, 4)
index = torch.tensor([[0, 1], [2, 3]])
torch.take(input, index)