'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
import torch
import numpy as np
"\nPyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, primarily developed by Facebook's AI Research lab (FAIR). It is free and open-source software released under the Modified BSD license.\n"
'\nGenerate input data\n'
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
a = torch.from_numpy(a)
b = torch.from_numpy(b)
'\nCall the API torch.clone\ntorch.clone(input, *, memory_format=torch.preserve_format)\n'
c = torch.clone(a)
print(c)
d = torch.clone(b)
print(d)