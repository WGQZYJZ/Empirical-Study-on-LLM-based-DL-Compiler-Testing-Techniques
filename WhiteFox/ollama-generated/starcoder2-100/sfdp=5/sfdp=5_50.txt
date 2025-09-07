
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, query, key, value):
        v1  = self.attn(query, key, value)[0]
        return v1

# Initializing the model