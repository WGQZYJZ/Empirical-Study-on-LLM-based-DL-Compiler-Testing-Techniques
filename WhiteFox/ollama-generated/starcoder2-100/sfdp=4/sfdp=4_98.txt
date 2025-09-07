
import torch.nn.functional as F
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        qk = <EMAIL>(key) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = F.linear(attn_weight, value)
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
q1  = torch.randn(8092, 3754) # shape: [batch size, sequence length]
k1  = torch.randn(8092, 3754) # shape: [batch size, sequence length]
 
# Input to the model - q and k
x1  = (q1, k1)
__output__  = m(*x1)

