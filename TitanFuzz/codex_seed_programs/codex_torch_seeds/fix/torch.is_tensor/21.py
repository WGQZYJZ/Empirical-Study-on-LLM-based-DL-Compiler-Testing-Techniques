'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)
result = torch.is_tensor(tensor)
print(result)