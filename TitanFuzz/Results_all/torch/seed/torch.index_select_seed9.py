x = torch.randn(3, 4)
indices = torch.tensor([0, 2])
y = torch.index_select(x, dim=0, index=indices)