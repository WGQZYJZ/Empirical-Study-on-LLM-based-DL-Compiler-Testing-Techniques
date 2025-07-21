'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
end = torch.tensor([[0.9, 0.8, 0.7], [0.6, 0.5, 0.4]])
weight = 0.5
torch.Tensor.lerp_(input_tensor, end, weight)
'\nTask 4: Call the API torch.lerp\ntorch.lerp(_input_tensor, end, weight)\n'
torch.lerp(input_tensor, end, weight)
'\nTask 5: Call the API torch.Tensor.lerp\ninput_tensor.lerp_(end, weight)\n'
input_tensor.lerp_(end, weight)