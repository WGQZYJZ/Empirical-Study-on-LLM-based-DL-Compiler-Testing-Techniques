if True:
    input_tensor = torch.rand(3, 3)
    print('Input tensor: ', input_tensor)
    torch.nn.init.eye_(input_tensor)
    print('Output tensor: ', input_tensor)