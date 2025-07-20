x = torch.rand(3, 3)
indices = torch.triu_indices(3, 3, offset=0, dtype=torch.long)