if True:
    input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)
    print('Input tensor: ', input_tensor)
    output_tensor = torch.Tensor.bitwise_right_shift_(input_tensor, 1)
    print('Output tensor: ', output_tensor)