
class Attention(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(self, query, key, value, attn_mask):
        qk  = torch.einsum('bmnk,bmj->bnmkj', [query, key]) / math.sqrt(query.size(-1))
        attn_weight  = F.softmax(qk + attn_mask, dim=-1)
        output = torch.einsum('nbmkj, bmnl -> nbml', [attn_weight, value]).reshape(*output.shape[:-2], -1) # Apply dropout to the softmax output
        return output


# Initializing the model
m  = Attention()
__init_params_count__ = sum(x.numel() for x in m.parameters())
 
# Input tensors to the model
q1, k1, v1 = torch.randn(30, 8, 64, 52), torch.randn(30, 8, 64, 64), torch.randn(30, 8, 64, 12)
 
# Masks to the model
m_mask = torch.ones((30, 64, 64))
m_mask[:, 15:, 7:] -= float('inf')

