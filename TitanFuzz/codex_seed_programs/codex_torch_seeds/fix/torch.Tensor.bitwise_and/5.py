'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
if True:
    import torch
    input_tensor = torch.randint(low=0, high=2, size=(10,), dtype=torch.uint8)
    other = torch.randint(low=0, high=2, size=(10,), dtype=torch.uint8)
    output_tensor = input_tensor.bitwise_and(other)
    print('input_tensor: ', input_tensor)
    print('other: ', other)
    print('output_tensor: ', output_tensor)