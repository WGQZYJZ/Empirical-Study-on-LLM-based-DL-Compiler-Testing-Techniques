
class Model(torch.nn.Module):
    def __init__(self, n_heads = 1, n_layers=1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, n_heads)
 
    def forward(self, query, key, value, scaled_qk):
        attn_output = self.attn(query, key, value)[0]
        return attn_output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
