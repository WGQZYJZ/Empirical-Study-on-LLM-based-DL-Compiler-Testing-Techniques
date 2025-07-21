'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
other_data = torch.randn(2, 3)
output_data = torch.hypot(input_data, other_data)
print(input_data)
print(other_data)
print(output_data)
expected_output = torch.empty(2, 3)
for i in range(input_data.size(0)):
    for j in range(input_data.size(1)):
        expected_output[(i, j)] = (((input_data[(i, j)] ** 2) + (other_data[(i, j)] ** 2)) ** 0.5)
print(expected_output)
print(torch.allclose(output_data, expected_output))