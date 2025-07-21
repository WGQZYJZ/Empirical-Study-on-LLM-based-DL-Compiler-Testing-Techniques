'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import torch
batch_size = 64
seq_len = 100
input_size = 512
hidden_size = 512
num_layers = 6
num_heads = 8
input_data = torch.randn(batch_size, seq_len, input_size)
encoder_layer = nn.TransformerEncoderLayer(input_size, num_heads, hidden_size)
transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers)
output = transformer_encoder(input_data)
print(output.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoder\ntorch.nn.TransformerDecoder(decoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn