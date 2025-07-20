if True:
    input_tensor = torch.randn(2, 3)
    print('input_tensor: ', input_tensor)
    output_tensor = torch.Tensor.cumsum_(input_tensor, dim=0)
    print('output_tensor: ', output_tensor)