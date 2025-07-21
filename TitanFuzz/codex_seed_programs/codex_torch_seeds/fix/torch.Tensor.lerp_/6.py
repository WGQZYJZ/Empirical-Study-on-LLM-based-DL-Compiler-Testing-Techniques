'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp_\ntorch.Tensor.lerp_(_input_tensor, end, weight)\n'
import torch
import torch
start = torch.tensor([1.0, 1.0, 1.0], dtype=torch.float32)
end = torch.tensor([2.0, 2.0, 2.0], dtype=torch.float32)
torch.Tensor.lerp_(start, end, weight=0.5)
print(start)