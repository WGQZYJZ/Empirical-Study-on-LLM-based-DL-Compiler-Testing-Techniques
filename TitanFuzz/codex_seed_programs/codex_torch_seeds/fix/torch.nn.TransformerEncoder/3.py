'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
X = torch.rand(10, 3, 8)
print(X.shape)
encoder_layer = nn.TransformerEncoderLayer(d_model=8, nhead=2)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=2)
output = encoder(X)
print(output.shape)