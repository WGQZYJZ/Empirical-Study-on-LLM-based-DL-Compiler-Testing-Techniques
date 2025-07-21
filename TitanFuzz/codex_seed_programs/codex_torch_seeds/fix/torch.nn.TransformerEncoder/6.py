'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
batch_size = 2
seq_len = 3
input_dim = 4
output_dim = 5
input_data = torch.randn(batch_size, seq_len, input_dim)
encoder_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=2)
encoder = nn.TransformerEncoder(encoder_layer, num_layers=2)
output = encoder(input_data)
print(output.shape)