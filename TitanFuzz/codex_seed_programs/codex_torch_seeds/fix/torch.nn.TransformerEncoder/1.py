'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
src = torch.randn(10, 32, 512)
trg = torch.randn(20, 32, 512)
encoder_layer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
encoder_norm = nn.LayerNorm(normalized_shape=512)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=6, norm=encoder_norm)
output = encoder(src)
print(output.size())