

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, query, key=None, value=None):
        v1 , v2 = self.attn(query, key, value) 
        return v1


# Initializing the model
m  = Model()
