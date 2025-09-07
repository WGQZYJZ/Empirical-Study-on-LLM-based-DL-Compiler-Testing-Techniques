
import torch
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0., attn_mask=None):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(d_model=128)
 
        self.dropout  = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query, key, value):
        qk = self.attn(query, key)[0]
        return qk


# Initializing the model