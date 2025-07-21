'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.not_equal\ntorch.Tensor.not_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.not_equal(input_tensor, other=torch.tensor(1))
print('input_tensor = \n{}'.format(input_tensor))
print('output_tensor = \n{}'.format(output_tensor))
'\nExpected output:\ninput_tensor =\ntensor([[1, 2],\n        [3, 4]])\noutput_tensor =\ntensor([[False,  True],\n        [ True,  True]])\n'
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.not_equal\ntorch.Tensor.not_equal(_input_tensor, other)\n'
import torch