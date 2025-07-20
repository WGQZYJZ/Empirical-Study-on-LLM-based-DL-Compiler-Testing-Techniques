if True:
    _input_tensor = torch.rand(10)
    _output_tensor = torch.Tensor.is_pinned(_input_tensor)
    print('PyTorch Version:', torch.__version__)
    print('Output Tensor:', _output_tensor)