'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoder\ntorch.nn.TransformerDecoder(decoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import numpy as np
batch_size = 4
seq_len = 8
num_heads = 4
dim = 16
num_layers = 2
decoder_input = torch.rand(batch_size, seq_len, dim)
memory = torch.rand(batch_size, seq_len, dim)
mask = torch.ones(batch_size, seq_len, seq_len)
decoder_layer = nn.TransformerDecoderLayer(dim, num_heads)
decoder = nn.TransformerDecoder(decoder_layer, num_layers)