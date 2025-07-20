input_data = torch.randn(2, 3)
output_data = torch.Tensor.diag_embed(input_data, offset=0, dim1=(- 2), dim2=(- 1))