'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
input_data = [1, 2, 3, 4, 5, 6]
tensor_dataset = torch.utils.data.TensorDataset(torch.tensor(input_data))
print(tensor_dataset[0])
print(tensor_dataset[0][0])
print(type(tensor_dataset))
print(len(tensor_dataset))