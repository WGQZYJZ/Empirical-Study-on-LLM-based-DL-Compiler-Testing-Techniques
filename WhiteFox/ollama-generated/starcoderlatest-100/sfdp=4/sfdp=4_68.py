
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1, 8)
 
    def forward(self, q1, k1, v1, attn_mask):
        # Multi-head attention computes a scaled dot product between the query and key using the query's attention mask
        # Note that unlike in normal linear layers, the output of this layer is transposed to be compatible with
        # multi-head attention.
        (attn_weight, _) = self.attn(q1, k1, v1, attn_mask)
 
        # Apply a softmax function over the result and transpose the result so that it matches the shape of input tensor
        return torch.softmax(attn_weight, dim=-2).transpose(-2, -1) @ v1


# Inputs to the model
q1 = torch.randn(50, 8, 64, 64)
k1 = torch.randn(50, 8, 64, 64)
v1 = torch.randn(50, 8, 64, 64)
attn_mask = (q1 == k1).byte() # attention mask has shape (50, 8, 64, 64), dtype: bool, values are `True` when the key is same as query.
 
# Applying the model
output = m(q1, k1, v1, attn_mask)


## Input tensor for user
import torch
import math
import numpy as np

def gen_random_tensor(shape):
    return torch.tensor(
        np.random.randn(*shape), 
        dtype=torch.float32, 
        requires_grad=True).cuda()

x1 = gen_random_tensor([50, 8, 64, 64])
output = m(x1)

