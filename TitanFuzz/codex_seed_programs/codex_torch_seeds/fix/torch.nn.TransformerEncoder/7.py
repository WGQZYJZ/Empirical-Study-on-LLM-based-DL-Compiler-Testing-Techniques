'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerEncoder\ntorch.nn.TransformerEncoder(encoder_layer, num_layers, norm=None)\n'
import torch
from torch.nn import TransformerEncoder, TransformerEncoderLayer
import torch
src = torch.rand((3, 4, 10))
encoder_layer = TransformerEncoderLayer(d_model=10, nhead=2)
model = TransformerEncoder(encoder_layer, num_layers=2)
output = model(src)
print(output.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoder\ntorch.nn.TransformerDecoder(decoder_layer, num_layers, norm=None)\n'
import torch
from torch.nn import TransformerDecoder, TransformerDecoderLayer
import torch
src = torch.rand((3, 4, 10))