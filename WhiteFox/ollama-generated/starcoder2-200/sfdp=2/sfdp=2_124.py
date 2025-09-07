
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att  = torch.nn.MultiheadAttention(d_model=64, num_heads=8)
 
    def forward(self, query, key, value):
        v1  = self.att(query, key, value)[0]
        return v1


# Initializing the model