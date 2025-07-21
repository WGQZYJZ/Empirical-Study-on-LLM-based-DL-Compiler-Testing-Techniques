'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.profiler.profile\ntorch.profiler.profile(*, activities=None, schedule=None, on_trace_ready=None, record_shapes=False, profile_memory=False, with_stack=False, with_flops=False, with_modules=False, use_cuda=None)\n'
import torch
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
torch.profiler.profile(activities=['cuda_memcpy_htod'], record_shapes=True, with_stack=True, with_flops=True, with_modules=True)
z = (x + y)
torch.profiler.profile(activities=['cuda_memcpy_htod'], record_shapes=True, with_stack=True, with_flops=True, with_modules=True)
z = (x + y)