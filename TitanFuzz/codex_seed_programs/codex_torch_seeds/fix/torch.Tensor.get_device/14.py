'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.get_device\ntorch.Tensor.get_device(_input_tensor)\n'
import torch
tensor_cpu = torch.rand(2, 3, 4)
tensor_gpu = torch.rand(2, 3, 4, device='cuda')
print(tensor_cpu.get_device())
print(tensor_gpu.get_device())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, device=None, dtype=None, non_blocking=False, copy=False)\n'
import torch
tensor_cpu = torch.rand(2, 3, 4)
tensor_gpu = torch.rand(2, 3, 4, device='cuda')
tensor_cpu_to_gpu = tensor_cpu.to('cuda')
tensor_gpu_to_cpu = tensor_gpu.to('cpu')
print(tensor_cpu_to_gpu.get_device())
print(tensor_gpu_to_cpu.get_device())