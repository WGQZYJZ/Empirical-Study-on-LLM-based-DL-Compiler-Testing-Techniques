
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.w  = torch.nn.Parameter(torch.randn((32, 64)))
        self.b  = torch.nn.Parameter(torch.randn((1025, 64)))
 
    def forward(self, q_k, value):
        attn_weight  = q_k @ self.w + self.b # Compute the attention weights by computing a dot product between query and key
        return (attn_weight * torch.softmax(q_k, dim=-1)) @ value # Use the softmax weights to compute a weighted sum of values


# Initializing the model 
a = Attention()

# Inputs to the model 
query   = torch.randn((32, 64)) 
key     = torch.randn( query.size())
value   = torch.randn( key.size())
mask    = torch.ones( (1025, ))
attn_mask  = ( mask * -1e9).reshape(1, -1)

__output__  = a(query @ key.transpose(-2, -1), value)

