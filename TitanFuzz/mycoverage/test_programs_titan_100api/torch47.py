import torch
data = torch.arange(0, 12, dtype=torch.float)
window = torch.hann_window(12)
output = torch.multiply(data, window)