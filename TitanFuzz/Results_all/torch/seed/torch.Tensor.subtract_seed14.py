if True:
    print('Task 1: import PyTorch')
    print('\nTask 2: Generate input data')
    input_tensor = torch.rand(3, 3)
    print('input_tensor: {}'.format(input_tensor))
    print('\nTask 3: Call the API torch.Tensor.subtract')
    output_tensor = torch.Tensor.subtract(input_tensor, 0.5)
    print('output_tensor: {}'.format(output_tensor))