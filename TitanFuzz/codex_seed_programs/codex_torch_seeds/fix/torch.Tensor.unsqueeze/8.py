'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
task1_input_data = torch.randn(2, 3)
print('Task 1 input data:\n', task1_input_data)
task2_input_data = torch.randn(2, 3)
print('Task 2 input data:\n', task2_input_data)
task3_input_data = torch.randn(2, 3)
print('Task 3 input data:\n', task3_input_data)
task3_output_data = task3_input_data.unsqueeze(0)
print('Task 3 output data:\n', task3_output_data)
task3_output_data = task3_input_data.unsqueeze(1)
print('Task 3 output data:\n', task3_output_data)
task3_output_data = task3_input_data.unsqueeze((- 1))
print('Task 3 output data:\n', task3_output_data)