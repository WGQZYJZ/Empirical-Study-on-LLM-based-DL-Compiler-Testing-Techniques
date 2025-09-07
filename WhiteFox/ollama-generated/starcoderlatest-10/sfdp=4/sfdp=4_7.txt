
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear_qk = torch.nn.Linear(dim, dim)
 
    def forward(self, q, k, v, mask=None):  # mask: optional positional mask that prevents attention to certain positions
        v = v + self.attn_bias
        attn = F.softmax(self.linear_qk(q).matmul(k), dim=-1)  # Compute the softmax of the dot product between the query and key
        attn *= (mask if mask is not None else 1)  # Mask out the irrelevant positions for computation
        
        return attn @ v
# Initializing the model
m = Attention(dim=64)


# Inputs to the model
query = torch.randn(3, 8, 64)
key = torch.randn(2, 16, 64)
value = torch.randn(3, 16, 64)
mask = torch.ones((3, 64))
attn_weight  = m(query, key, value, mask)


