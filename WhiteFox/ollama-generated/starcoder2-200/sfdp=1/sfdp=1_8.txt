
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(10, 3)
 
    def forward(self, query, key, value):
        v1, v2  = self.attn(query, key, value)
        return v2


# Initializing the model