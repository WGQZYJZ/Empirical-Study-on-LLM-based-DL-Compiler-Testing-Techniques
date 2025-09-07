
class Model(torch.nn.Module):
    def __init__(self, query, key, value):
        super().__init__()
        self.q  = torch.nn.Parameter(query) # A learnable query tensor
        self.k  = torch.nn.Parameter(key)   # A learnable key tensor
        self.v  = torch.nn.Parameter(value) # A learnable value tensor
 
    def forward(self, attn_mask=None):
        qk = self.q @ self.k.transpose(-2, -1) / math.sqrt(self.q.size(-1))
        qk += attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p, True) # apply dropout to the softmax output
        output = attn_weight @ self.v 
        return output

# Initializing the model and its inputs/parameters
query = torch.randn(8096, 768) / math.sqrt(32)
key   = query
value = key
attn_mask = torch.nn.Parameter(torch.randn(1, 512)) # A learnable attention mask that contains one element per input dimension and is used as an addition in the dot product operation.
m      = Model(query, key, value)

