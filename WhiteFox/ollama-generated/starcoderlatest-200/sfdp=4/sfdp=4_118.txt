
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 64)
 
    def forward(self, query, key, value, attn_mask):
        v1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask
        v2 = torch.softmax(v1, dim=-1)
        output = (attn_weight * value).sum(dim=1)
        return output

# Initializing the model
m = Model()

 # Query tensor
q  = torch.randn(8, 64)
 
 # Key tensor
k  = torch.randn(16, 64)
 
 # Value tensor
v  = torch.randn(32, 64)

 # Attention mask tensor
m  = torch.ones((16, 8))

 # Inputs to the model
