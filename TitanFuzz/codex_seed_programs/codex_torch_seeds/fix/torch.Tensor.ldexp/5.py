'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp\ntorch.Tensor.ldexp(_input_tensor, other)\n'
import torch
tensor_input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Tensor input: ', tensor_input)
tensor_result = tensor_input.ldexp(2)
print('Tensor result: ', tensor_result)
tensor_input = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Tensor input: ', tensor_input)
tensor_result = tensor_input.ldexp(4)
print('Tensor result: ', tensor_result)