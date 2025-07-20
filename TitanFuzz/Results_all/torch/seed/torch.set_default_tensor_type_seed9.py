if True:
    print('PyTorch version:', torch.__version__)
    input_data = torch.rand(2, 3)
    print('Input data:', input_data)
    torch.set_default_tensor_type(torch.DoubleTensor)
    print('Tensor type:', input_data.type())