"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoderLayer\ntorch.nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-05, batch_first=False, device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
src = torch.randn(64, 10, 512)
tgt = torch.randn(64, 10, 512)
memory = torch.randn(64, 10, 512)
transformer_decoder_layer = nn.TransformerDecoderLayer(512, 8, 2048)
output = transformer_decoder_layer(tgt, memory)
print(output.shape)