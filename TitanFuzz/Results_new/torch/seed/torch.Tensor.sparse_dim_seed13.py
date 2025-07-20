if True:
    import torch
    _input_tensor = torch.randn((2, 3))
    print('Input tensor:')
    print(_input_tensor)
    _sparse_dim = torch.Tensor.sparse_dim(_input_tensor)
    print('Output sparse_dim:')
    print(_sparse_dim)