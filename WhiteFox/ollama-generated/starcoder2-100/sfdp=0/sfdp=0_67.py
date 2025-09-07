
import torch
import torch.nn as nn
from pytorch_pretrained_bert import BertModel


class MyTransformer(torch.nn.Module):
    def __init__(self, embedding_dim=768, num_heads=12, d_ff=512):
        super().__init__()

        self._encoder = torch.nn.TransformerEncoderLayer(d_model=embedding_dim, nhead=num_heads)
        self._decoder = torch.nn.TransformerDecoderLayer(d_model=embedding_dim, nhead=num_heads)

        self._pos_enc = nn.Parameter(torch.zeros(1024*768))


    def forward(self):
        return self


class Bert(BertModel):
    def __init__(self):
      super().__init__()

      # This is the transformer module
      self.encoder = MyTransformer()

    def forward(self, x):
         return self.encoder(x)


model = Bert().cuda()
input_ids  = torch.zeros((128,32), dtype=torch.int).cuda() # input ids

model(input_ids)
