if True:
    input_tensor = torch.randn(4, 3, 2)
    print('Input tensor: ', input_tensor)
    result_tensor = torch.Tensor.movedim(input_tensor, 0, 1)
    print('Result tensor: ', result_tensor)