'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
input_data = [1, 2, 3, 4, 5]
input_data_tensor = torch.tensor(input_data)
print('input_data_tensor: ', input_data_tensor)
test_elements = [1, 2, 3, 4, 5]
test_elements_tensor = torch.tensor(test_elements)
print('test_elements_tensor: ', test_elements_tensor)
result = torch.isin(input_data_tensor, test_elements_tensor)
print('result: ', result)