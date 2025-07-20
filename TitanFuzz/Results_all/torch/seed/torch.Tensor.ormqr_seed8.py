if True:
    print('Task 1: import PyTorch')
    print('Task 2: Generate input data')
    input_tensor = torch.randn(2, 3, 4)
    input2 = torch.randn(2, 3, 4)
    input3 = torch.randn(2, 3, 4)
    print('Task 3: Call the API torch.Tensor.ormqr')
    output = torch.Tensor.ormqr(input_tensor, input2, input3, left=True, transpose=False)
    print('output: {}'.format(output))