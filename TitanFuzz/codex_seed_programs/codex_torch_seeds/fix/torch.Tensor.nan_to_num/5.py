'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[float('nan'), float('inf'), (- float('inf'))], [float('nan'), float('inf'), (- float('inf'))]])
_output_tensor = torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)