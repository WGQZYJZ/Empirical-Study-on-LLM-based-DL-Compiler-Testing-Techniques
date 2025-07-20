input_tensor = torch.randn(3, 3, 3)
output_tensor = torch.Tensor.diag_embed(input_tensor, offset=0, dim1=(- 2), dim2=(- 1))