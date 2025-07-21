'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
import torch
input_data = Variable(torch.randn(2, 3))
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cosine_similarity(input_data, input_data)
print(output)