input_tensor = torch.randn((2, 3, 4, 5))
result = torch.Tensor.diag_embed(input_tensor, offset=0, dim1=(- 2), dim2=(- 1))