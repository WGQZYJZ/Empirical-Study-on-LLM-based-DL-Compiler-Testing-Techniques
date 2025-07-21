'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isfinite\ntorch.Tensor.isfinite(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[float('inf'), float('-inf')], [float('nan'), float('nan')]])
isfinite_result = input_tensor.isfinite()
print('isfinite_result: ', isfinite_result)