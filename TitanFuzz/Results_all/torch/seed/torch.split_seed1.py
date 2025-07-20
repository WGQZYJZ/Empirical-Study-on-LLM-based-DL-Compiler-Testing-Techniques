tensor = torch.randn(2, 3, 4)
result = torch.split(tensor, split_size_or_sections=2, dim=0)