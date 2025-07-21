if True:
    print('PyTorch version: ', torch.__version__)
    print('cuDNN version: ', torch.backends.cudnn.version())
    print('Torchvision version: ', torchvision.__version__)
    inputs = torch.randn(2, 3, 5)
    print('Input data: ', inputs)
    torch.hub.set_dir('/tmp/my_dir')
    print('PyTorch version: ', torch.__version__)