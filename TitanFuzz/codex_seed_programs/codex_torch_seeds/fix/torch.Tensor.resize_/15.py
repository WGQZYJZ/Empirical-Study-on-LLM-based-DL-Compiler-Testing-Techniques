'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
if True:
    input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print('Input tensor:')
    print(input_tensor)
    resized_tensor = input_tensor.resize_(2, 3)
    print('Resized tensor:')
    print(resized_tensor)