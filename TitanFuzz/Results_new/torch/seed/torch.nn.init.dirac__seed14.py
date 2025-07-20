if True:
    import torch
    input_data = torch.rand(2, 2, 2)
    print('Input data: ', input_data)
    torch.nn.init.dirac_(input_data, groups=1)
    print('Output data: ', input_data)