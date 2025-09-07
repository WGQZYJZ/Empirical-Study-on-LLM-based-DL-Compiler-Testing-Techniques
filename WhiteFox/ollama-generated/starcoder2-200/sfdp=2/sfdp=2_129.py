
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, 1)
 
    def forward(self, x1, x2):
        v1 = query
        v2 = key
        v3 = value
        v4 = self.attn(v1, v2)[0] # The output of the attention is the third parameter
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 8)
x2 = x1 + torch.randn(3, 8)
