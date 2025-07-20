input = torch.rand(2, 3, 4)
output = torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))