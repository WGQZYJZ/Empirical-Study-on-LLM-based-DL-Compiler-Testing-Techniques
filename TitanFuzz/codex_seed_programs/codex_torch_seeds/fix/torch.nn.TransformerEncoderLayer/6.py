"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoderLayer\ntorch.nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-05, batch_first=False, device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
batch_size = 64
input_dim = 512
seq_len = 80
input_tensor = torch.randn(batch_size, seq_len, input_dim)
encoder_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=8)
encoder_norm = nn.LayerNorm(input_dim)
output_tensor = encoder_layer(input_tensor)
print(output_tensor.shape)