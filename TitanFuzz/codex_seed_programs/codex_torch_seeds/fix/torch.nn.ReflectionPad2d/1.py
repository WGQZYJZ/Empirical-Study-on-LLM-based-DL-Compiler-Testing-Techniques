'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
input = torch.tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]]], dtype=torch.float32)
pad = torch.nn.ReflectionPad2d((1, 1, 1, 1))
output = pad(input)
print(output)
print(output.shape)