'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.poisson\ntorch.poisson(input, generator=None)\n'
import torch
import torch
input = torch.rand(1, 1)
input
torch.poisson(input, generator=None)
new_generator = torch.Generator()
new_generator.manual_seed(12345)
torch.poisson(input, generator=new_generator)
new_generator = torch.Generator()
new_generator.manual_seed(12346)
torch.poisson(input, generator=new_generator)
new_generator = torch.Generator()
new_generator.manual_seed(12347)
torch.poisson(input, generator=new_generator)