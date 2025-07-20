if True:
    input_tensor = torch.randn(2, 3)
    other = torch.randn(3, 2)
    print('input_tensor: ', input_tensor)
    print('other: ', other)
    print('torch.Tensor.vdot(_input_tensor, other): ', torch.Tensor.vdot(input_tensor, other))