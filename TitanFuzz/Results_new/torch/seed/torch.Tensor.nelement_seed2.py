if True:
    _input_tensor = torch.rand(2, 3)
    _output = torch.Tensor.nelement(_input_tensor)
    print('The input tensor is:', _input_tensor)
    print('The output of nelement is:', _output)