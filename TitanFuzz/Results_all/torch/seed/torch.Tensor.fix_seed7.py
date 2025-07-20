if True:
    _input_tensor = torch.ones(3, 3, dtype=torch.float32)
    print('Before calling fix API: {}'.format(_input_tensor))
    _output_tensor = torch.Tensor.fix(_input_tensor)
    print('After calling fix API: {}'.format(_output_tensor))