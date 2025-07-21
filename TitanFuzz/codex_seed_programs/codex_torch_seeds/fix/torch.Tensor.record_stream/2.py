'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.record_stream\ntorch.Tensor.record_stream(_input_tensor, stream\n'
import torch
import torch.cuda
input_tensor = torch.randn(2, 3, 4)
stream = torch.cuda.Stream()
with torch.cuda.stream(stream):
    output_tensor = input_tensor.record_stream(stream)
stream.synchronize()
print(output_tensor)
print(input_tensor)