"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoderLayer\ntorch.nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-05, batch_first=False, device=None, dtype=None)\n"
import torch
import torch.nn as nn
d_model = 512
nhead = 8
dim_feedforward = 2048
batch_size = 64
max_seq_len = 100
src = torch.rand(batch_size, max_seq_len, d_model)
tgt = torch.rand(batch_size, max_seq_len, d_model)
layers = nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward)
output = layers(tgt, src)
print(output.size())