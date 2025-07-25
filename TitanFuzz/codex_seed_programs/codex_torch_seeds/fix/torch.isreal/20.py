'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isreal\ntorch.isreal(input)\n'
import torch
input1 = torch.tensor([1, 2, 3])
input2 = torch.tensor([1, 2, 3], dtype=torch.float32)
input3 = torch.tensor([1, 2, 3], dtype=torch.float64)
input4 = torch.tensor([1, 2, 3], dtype=torch.complex64)
output1 = torch.isreal(input1)
output2 = torch.isreal(input2)
output3 = torch.isreal(input3)
output4 = torch.isreal(input4)
print('input1:', input1)
print('output1:', output1)
print('input2:', input2)
print('output2:', output2)
print('input3:', input3)
print('output3:', output3)
print('input4:', input4)
print('output4:', output4)