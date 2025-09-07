
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask=None):
        v1  = self.attn(query, key, value)
        return v1

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(2048, 65536)
key    = torch.randn(2048, 65536)
value  = torch.randn(2048, 65536)

