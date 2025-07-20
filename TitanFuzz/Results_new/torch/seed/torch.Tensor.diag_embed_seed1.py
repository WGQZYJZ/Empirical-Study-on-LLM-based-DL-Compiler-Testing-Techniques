input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output_tensor = torch.Tensor.diag_embed(input_tensor, offset=0, dim1=(- 2), dim2=(- 1))