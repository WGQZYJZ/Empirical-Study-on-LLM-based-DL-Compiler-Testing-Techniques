'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm_\ntorch.Tensor.baddbmm_(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
(batch_size, num_features, num_hidden) = (64, 100, 50)
x = torch.randn(batch_size, num_features)
w1 = torch.randn(num_features, num_hidden)
w2 = torch.randn(num_hidden, num_hidden)
h = torch.zeros(batch_size, num_hidden)
h.baddbmm_(x, w1, w2)
print(h)