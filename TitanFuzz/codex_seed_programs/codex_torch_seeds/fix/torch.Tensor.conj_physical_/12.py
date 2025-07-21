'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical_\ntorch.Tensor.conj_physical_(_input_tensor)\n'
import torch
if True:
    import torch
    input_tensor = torch.randint(low=0, high=10, size=(3, 4), dtype=torch.int32)
    print('Input: ', input_tensor)
    torch.Tensor.conj_physical_(input_tensor)
    print('Output: ', input_tensor)