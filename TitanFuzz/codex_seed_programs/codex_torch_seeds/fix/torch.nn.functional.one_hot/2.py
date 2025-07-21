'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import torch
input_data = torch.tensor([2, 1, 0])
output_data = torch.nn.functional.one_hot(input_data, num_classes=3)
print(output_data)
assert torch.all(torch.eq(output_data, torch.tensor([[0, 0, 1], [0, 1, 0], [1, 0, 0]]))), 'Wrong result, please check your code'
print('Correct')
output_data = torch.nn.functional.one_hot(input_data, num_classes=4)
print(output_data)