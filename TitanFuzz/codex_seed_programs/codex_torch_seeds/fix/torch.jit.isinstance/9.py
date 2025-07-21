'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
input_data = torch.rand(1, 2, 3)
torch.jit.isinstance(input_data, torch.Tensor)
torch.jit.isinstance(input_data, torch.FloatTensor)
torch.jit.isinstance(input_data, torch.DoubleTensor)
torch.jit.isinstance(input_data, torch.HalfTensor)
torch.jit.isinstance(input_data, torch.ByteTensor)
torch.jit.isinstance(input_data, torch.CharTensor)
torch.jit.isinstance(input_data, torch.ShortTensor)
torch.jit.isinstance(input_data, torch.IntTensor)
torch.jit.isinstance(input_data, torch.LongTensor)