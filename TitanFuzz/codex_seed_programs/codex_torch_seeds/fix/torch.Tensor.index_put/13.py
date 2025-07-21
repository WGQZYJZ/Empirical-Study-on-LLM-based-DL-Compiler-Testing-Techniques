'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
_input_tensor = torch.randint(1, 10, (3, 3))
print('Input tensor: ', _input_tensor)
_indices = torch.tensor([[0, 0], [1, 1], [2, 2]])
_values = torch.tensor([11, 22, 33])
_output_tensor = torch.zeros_like(_input_tensor)
_output_tensor.index_put((_indices,), _values, accumulate=False)
print('Output tensor: ', _output_tensor)