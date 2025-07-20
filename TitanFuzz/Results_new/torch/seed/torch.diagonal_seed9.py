if True:
    input_data = torch.arange(1, 17).view(4, 4)
    print('Input data:\n', input_data)
    print('\nDiagonal elements: ', torch.diagonal(input_data))
    print('Diagonal elements, offset=1: ', torch.diagonal(input_data, offset=1))
    print('Diagonal elements, offset=-1: ', torch.diagonal(input_data, offset=(- 1)))
    print('Diagonal elements, offset=1, dim1=1, dim2=0: ', torch.diagonal(input_data, offset=1, dim1=1, dim2=0))