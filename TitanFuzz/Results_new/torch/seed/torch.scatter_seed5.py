input = torch.randn(3, 5)
torch.scatter(input, 1, torch.tensor([[4], [3], [1]]), 1)