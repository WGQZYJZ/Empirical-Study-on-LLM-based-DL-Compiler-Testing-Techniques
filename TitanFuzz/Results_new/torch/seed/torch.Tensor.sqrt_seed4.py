if True:
    input_tensor = torch.randn(1, 3)
    output_tensor = torch.Tensor.sqrt(input_tensor)
    print('Input tensor: {}'.format(input_tensor))
    print('Output tensor: {}'.format(output_tensor))