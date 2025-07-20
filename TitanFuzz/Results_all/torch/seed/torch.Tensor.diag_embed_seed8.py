input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.diag_embed(input_tensor, offset=1, dim1=(- 2), dim2=(- 1))