input_data = torch.arange(1, 17).view(4, 4)
diagonal_data = torch.diagonal(input_data)
diagonal_data = torch.diagonal(input_data, offset=1)
diagonal_data = torch.diagonal(input_data, offset=(- 1))
diagonal_data = torch.diagonal(input_data, offset=1, dim1=0, dim2=1)
diagonal_data = torch.diagonal(input_data, offset=(- 1), dim1=0, dim2=1)