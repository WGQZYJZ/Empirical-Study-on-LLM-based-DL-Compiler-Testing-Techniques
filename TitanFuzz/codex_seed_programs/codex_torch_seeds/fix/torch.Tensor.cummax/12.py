'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
_input_tensor = torch.rand(2, 3)
cummax_result = _input_tensor.cummax(dim=1)
print('cummax_result = ', cummax_result)
'\nExpected output:\ncummax_result =  tensor([[0.3589, 0.3589, 0.3589],\n        [0.9086, 0.9086, 0.9086]])\n'