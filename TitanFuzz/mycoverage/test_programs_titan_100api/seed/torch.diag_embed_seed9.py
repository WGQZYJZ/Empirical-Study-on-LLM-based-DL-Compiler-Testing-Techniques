input = torch.arange(1, 7).view(2, 3)
output = torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))