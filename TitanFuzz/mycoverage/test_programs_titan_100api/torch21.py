import torch
input_data = torch.tensor([[1, 2, (- 1), (- 2)], [1, (- 1), 1, (- 1)], [(- 1), 1, (- 1), 1]], dtype=torch.float32)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
output = prelu(input_data)