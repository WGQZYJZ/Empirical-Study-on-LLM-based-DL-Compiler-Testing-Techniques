input = torch.randn(3, 3)
output = torch.diag_embed(input, offset=0, dim1=(- 2), dim2=(- 1))