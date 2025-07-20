if True:
    print('Task 1: import PyTorch')
    print('Task 2: Generate input data')
    input_tensor = torch.randn(4, 4)
    print('input_tensor: ', input_tensor)
    print('Task 3: Call the API torch.Tensor.narrow')
    output_tensor = torch.Tensor.narrow(input_tensor, 0, 0, 3)
    print('output_tensor: ', output_tensor)