'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=255, size=(3, 3), dtype=torch.uint8)
print('input_tensor:', input_tensor)
q_zero_point = input_tensor.q_zero_point()
print('q_zero_point:', q_zero_point)