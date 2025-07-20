input = torch.randn(3, 5)
torch.scatter(input, 1, torch.tensor([[4, 1, 2], [3, 0, 0]]), 0.5)