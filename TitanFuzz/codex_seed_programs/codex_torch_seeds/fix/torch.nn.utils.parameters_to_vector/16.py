'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
input_data = [torch.randn(1, 3, 224, 224), torch.randn(1, 3, 224, 224)]
vector = torch.nn.utils.parameters_to_vector(input_data)
print(vector)