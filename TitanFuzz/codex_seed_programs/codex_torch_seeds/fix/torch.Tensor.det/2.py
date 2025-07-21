'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
'\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
if True:
    print('===== Task 1: import PyTorch =====')
    print('torch.__version__: ', torch.__version__)
    print('===== Task 2: Generate input data =====')
    input_tensor = torch.tensor([[1, 2], [3, 4]])
    print('input_tensor: ', input_tensor)
    print('===== Task 3: Call the API torch.Tensor.det =====')
    print('torch.Tensor.det(input_tensor): ', torch.Tensor.det(input_tensor))