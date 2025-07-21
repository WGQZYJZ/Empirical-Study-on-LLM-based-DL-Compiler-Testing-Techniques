'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_result = _input_tensor.apply_((lambda x: (x * 2)))
print('Result: ', _result)