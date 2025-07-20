if True:
    input_tensor = torch.randn(2, 3)
    print('input_tensor: ', input_tensor)
    output_tensor = torch.Tensor.i0(input_tensor)
    print('output_tensor: ', output_tensor)