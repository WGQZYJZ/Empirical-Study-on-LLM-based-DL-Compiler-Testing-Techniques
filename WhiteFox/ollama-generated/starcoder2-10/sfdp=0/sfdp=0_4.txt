
import torch
 
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    @staticmethod
    def scaled_dot_product(q, k, v):
         inv_scale  = q.shape[-1] ** -0.5
         return (torch.matmul(query, key.transpose(-2, -1)) / inv_scale).softmax(dim=-1)
 
    def forward(self, query, key, value):
        attention_weights = ScaledDotProductAttention.scaled_dot_product(query, key, value)
        output  = attention_weights.matmul(value)
        return v6

