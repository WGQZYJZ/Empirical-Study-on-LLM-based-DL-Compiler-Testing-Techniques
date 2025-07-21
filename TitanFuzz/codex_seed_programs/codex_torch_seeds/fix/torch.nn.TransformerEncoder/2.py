'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
batch_size = 4
src_len = 10
tgt_len = 12
d_model = 512
d_inner = 1024
n_head = 8
num_layers = 6
src = torch.randn(batch_size, src_len, d_model)
tgt = torch.randn(batch_size, tgt_len, d_model)
encoder_layer = nn.TransformerEncoderLayer(d_model, n_head, d_inner, dropout=0.1)
encoder = nn.TransformerEncoder(encoder_layer, num_layers)
output = encoder(src)
print(output.shape)