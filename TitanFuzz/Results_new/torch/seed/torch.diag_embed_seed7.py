input = torch.randn(2, 3, 4)
result = torch.diag_embed(input, offset=1, dim1=(- 2), dim2=(- 1))