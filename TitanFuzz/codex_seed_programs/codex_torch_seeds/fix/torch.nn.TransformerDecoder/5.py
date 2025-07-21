'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.TransformerDecoder\ntorch.nn.TransformerDecoder(decoder_layer, num_layers, norm=None)\n'
import torch
from torch import nn
from torch.nn import TransformerDecoder, TransformerDecoderLayer
import torch
src = torch.rand(10, 32, 512)
tgt = torch.rand(20, 32, 512)
memory_key_padding_mask = torch.ByteTensor(32, 10).bernoulli_()
decoder_layer = TransformerDecoderLayer(d_model=512, nhead=8)
decoder = TransformerDecoder(decoder_layer, num_layers=6)
out = decoder(tgt, memory=src, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None, memory_key_padding_mask=memory_key_padding_mask)
print(out.size())