'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cuda\ntorch.Tensor.cuda(_input_tensor, device=None, non_blocking=False, memory_format=torch.preserve_format)\n'
import torch
if True:
    device = torch.device(('cuda' if torch.cuda.is_available() else 'cpu'))
    input_tensor = torch.randn(3, 3)
    cuda_input_tensor = input_tensor.cuda()
    print(cuda_input_tensor)