'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num_\ntorch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[1.0, float('nan'), float('inf')], [float('-inf'), 2.0, float('nan')]], dtype=torch.float32)
_nan_to_num_output = torch.Tensor.nan_to_num_(_input_tensor, nan=0.0, posinf=None, neginf=None)
print('input tensor: ', _input_tensor)
print('output tensor: ', _nan_to_num_output)