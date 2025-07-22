import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class Transformer(nn.Module):

    def __init__(self, n_heads: int, embed_dim: int) -> None:
        super().__init__()
        self.embedding = nn.Embedding(2003, embed_dim)
        self.pos_encoder = PositionalEncoding(embed_dim)
        encoder_layer = TransformerEncoderLayer(embed_dim, n_heads)
        self.transformer_encoder = TransformerEncoder(encoder_layer, 10)
        decoder_layer = TransformerDecoderLayer(embed_dim, n_heads)
        self.transformer_encoder = TransformerEncoder(decoder_layer, 10)

    def forward(self, src: Tensor, tgt: Tensor, src_mask: Tensor, tgt_mask: Tensor) -> Tensor:
        out = self.embedding(src) * math.sqrt(self.embed_dim)
        out = self.pos_encoder(out)
        encoder_out = self.transformer_encoder(out, src_mask)
        out2 = self.embedding(tgt) * math.sqrt(self.embed_dim)
        out2 = self.pos_encoder(out2)
        decoder_out = self.transformer_encoder(out2, src_mask, tgt_mask)
        return encoder_out


n_heads = 1
embed_dim = 1

func = Transformer(n_heads, embed_dim).to('cuda')


src = torch.eye(15, 20)

tgt = torch.eye(15, 20)
src_mask = 1
tgt_mask = 1

test_inputs = [src, tgt, src_mask, tgt_mask]
