
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, qk, v, k, v_mask=None, attn_mask=None):
        kq = qk @ k.transpose(-1, -2) / math.sqrt(qk.size(-1)) # Compute the dot product of query and key
        if v_mask is not None:
            vq = torch.einsum('bqhd,bvh->bhvq', (kq, v)) + v_mask  # Add the optional mask to the result of the dot product
        else:
            vq = torch.einsum('bqhd,bvhd->bhvq', (kq, v))
        attn_weight = self.attn(vq, k=k, v=v)[0] # Apply multihead attention
        if attn_mask is not None:
            attn_weight = attn_weight + attn_mask  # Add the optional mask to the result of attention
        return torch.einsum('bhv,bvhd->bhqd', (attn_weight, v))


# Initializing the model
m = Model()


# Inputs to the model
qk  = torch.randn(2, 8, 128, 3)
v   = torch.randn(8, 8, 64, 64)
k   = torch.randn(16, 8, 64, 64)
attn_mask = torch.ones(1, 2, 64, 64)
