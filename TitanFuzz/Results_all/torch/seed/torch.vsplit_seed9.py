input = torch.arange(start=0, end=18, step=1).view(3, 2, 3)
indices_or_sections = [2, 2]
output = torch.vsplit(input, indices_or_sections)