import torch
from torch import nn

class ScaledDotProductAttention(nn.Module):
    def __init__(self, d=768):
        super().__init__()
        self.dropout  = nn.Dropout()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: torch.Tensor) -> tuple:
 
        qk  = torch.einsum('iabh,ibjh->iajb', [query, key]) / math.sqrt(query.size(-1))
        qk  += attn_mask
        
        # Compute attention weights and scale
        attn_weight  = nn.Softmax(qk)
 
        output  = nn.Dropout()
 
        # Apply softmax to the result
        return qk, torch.einsum('iajb->ibj', [attn_weight]), value


class BertEncoderBlock(nn.Module):
 
    def __init__(self, d=768, n=12):  # Number of transformer encoder blocks. We set the block size to 12 for BERT.
        super().__init__()

        self.layer = nn.Sequential()
 
        for i in range(n):
            self.layer += nn.TransformerEncoderLayer(d_model=768, nhead=4)

    def forward(self, x):
 
        for i in range(len(self.layer)):
            layer  = self.layer[i]
            
            # Compute dot product attention
            qk, attn_weight, value  = layer(query=x, key=x, value=x, attn_mask=x)

            # Scale the result using scaled dot-product attention
            scale  = torch.div(torch.max(qk), 3e10).expand_as(value)

            x  = torch.mul(scale, value)
 
        return x
