
import torch, random
from math import sqrt
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1=None, v1=None):
        batch = len(q1)
 
        # Randomly generate keys and values if not passed in
        keys  = [torch.randn((batch, 50), dtype=torch.double) / sqrt(ksize[i]) for i in range(3)] 
        keys += [torch.randn((batch, ksize[0], 64)) * torch.nn.Parameter(torch.eye(64, device='cuda'))]
        keys = list(map(lambda t: t.to('cuda'), keys))
        values = [torch.rand(k1.shape) for i in range(3)] + [None] 
        values = tuple(filter(lambda v: v is not None and len(v), values))
 
        # Apply attention to the keys and values
        q, k, v  = torch.meshgrid(*keys)[0].transpose(-2, -1) 
        attn_mask  = torch.randn((batch * 3, 50)).cuda()
        qk = q @ k.transpose(-2, -1) / sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + attn_mask[:, None, :], dim=-1).cuda()
 
        # Apply dropout to the attention weights
        attn_weight = torch.dropout(attn_weight, 0.3)
 
        # Compute output
        o  = v @ attn_weight[None] 
        return tuple(o), attn_weight

