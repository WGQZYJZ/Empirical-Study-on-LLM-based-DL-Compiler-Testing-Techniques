'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.CosineSimilarity\ntorch.nn.CosineSimilarity(dim=1, eps=1e-08)\n'
import torch
import numpy as np
np.random.seed(0)
x = torch.from_numpy(np.random.rand(3, 4))
y = torch.from_numpy(np.random.rand(3, 4))
print(x)
print(y)
cosine_similarity = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
print(cosine_similarity(x, y))