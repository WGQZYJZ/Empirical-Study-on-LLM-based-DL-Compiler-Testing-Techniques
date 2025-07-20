x = torch.randn(4, 5)
torch.index_select(x, 0, torch.tensor([0, 3]))
torch.index_select(x, 1, torch.tensor([0, 3]))