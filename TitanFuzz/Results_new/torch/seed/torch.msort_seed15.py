if True:
    print('PyTorch version:', torch.__version__)
    x = torch.randn(3, 4)
    print('Input data x:', x)
    y = torch.msort(x)
    print('Output data y:', y)