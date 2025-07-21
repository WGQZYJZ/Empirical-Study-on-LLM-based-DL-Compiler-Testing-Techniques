'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
weight = torch.ones(3, requires_grad=True)
bias = torch.ones(1, requires_grad=True)
vector = nn.utils.parameters_to_vector([weight, bias])
print(vector)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.vector_to_parameters\ntorch.nn.utils.vector_to_parameters(vector, parameters)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F