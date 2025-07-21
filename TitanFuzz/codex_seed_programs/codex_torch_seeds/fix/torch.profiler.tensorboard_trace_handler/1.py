'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.profiler.tensorboard_trace_handler\ntorch.profiler.tensorboard_trace_handler(dir_name, worker_name=None, use_gzip=False)\n'
import torch
input = torch.rand(1, 3, 224, 224)
torch.profiler.tensorboard_trace_handler('./traces', 'resnet50', True)