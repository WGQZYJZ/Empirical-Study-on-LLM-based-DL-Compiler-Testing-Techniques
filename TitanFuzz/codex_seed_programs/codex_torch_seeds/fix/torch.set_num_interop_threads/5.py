'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
import time
input_size = (1, 3, 224, 224)
input_data = torch.rand(input_size)
torch.set_num_interop_threads(1)
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
model.eval()
for i in range(2):
    start = time.perf_counter()
    output = model(input_data)
    end = time.perf_counter()
    print('Elapsed time: {}'.format((end - start)))
for i in range(100):
    start = time.perf_counter()
    output = model(input_data)
    end = time.perf_counter()
    print('Elapsed time: {}'.format((end - start)))