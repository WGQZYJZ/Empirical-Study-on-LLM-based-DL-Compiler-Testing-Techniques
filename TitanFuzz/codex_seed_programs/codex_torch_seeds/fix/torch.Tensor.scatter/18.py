'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
if True:
    print('Task 1: import PyTorch')
    print('\nTask 2: Generate input data')
    input_tensor = torch.randn(2, 3)
    print('input_tensor =', input_tensor)
    print('\nTask 3: Call the API torch.Tensor.scatter')
    dim = 0
    index = torch.tensor([0, 1])
    src = torch.tensor([[1, 2, 3], [4, 5, 6]])
    output_tensor = input_tensor.scatter(dim, index, src)
    print('output_tensor =', output_tensor)