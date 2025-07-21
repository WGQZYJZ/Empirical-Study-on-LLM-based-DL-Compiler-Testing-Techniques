'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoder\ntorch.nn.TransformerDecoder(decoder_layer, num_layers, norm=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
batch_size = 64
seq_len = 10
input_dim = 20
output_dim = 20
input_data = torch.randn(batch_size, seq_len, input_dim)
output_data = torch.randn(batch_size, seq_len, output_dim)
decoder_layer = nn.TransformerDecoderLayer(d_model=input_dim, nhead=4)
decoder = nn.TransformerDecoder(decoder_layer, num_layers=1)
output = decoder(input_data, output_data)
print(output)