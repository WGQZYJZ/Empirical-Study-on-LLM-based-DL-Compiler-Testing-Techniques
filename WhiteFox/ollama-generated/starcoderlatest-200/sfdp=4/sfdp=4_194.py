
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask):
        qk  = torch.einsum("bcd,bc->bcd", (query, key)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  += attn_mask    # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)          # Apply softmax to the result
        output = torch.einsum("bcd,bc->bcd", (attn_weight, value)) # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
query  = torch.randn(32, 8, 64) # query: [32, 8, 64]
key    = torch.randn(32, 16, 64) # key:   [32, 16, 64]
value  = torch.randn(32, 16, 64) # value: [32, 16, 64]
attn_mask  = (torch.arange(32).view(-1, 1, 1) <= torch.arange(16)).float()   # attn_mask: [[[0., 1., 1., ..., 1.],...,[1., 1., 1., ..., 1.]]]
