
class Model(torch.nn.Module):
    def __init__(self, n_heads=128, dropout_p=0.5, scale_factor=4):
        super().__init__()
        self.scale_factor = torch.tensor(float(scale_factor))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.norm1  = torch.nn.LayerNorm(32 * n_heads)
 
    def forward(self, query, key):
         v0 = torch.matmul(query, key.transpose(-2, -1))
         v1 = v0 / self.scale_factor
         v2 = v1.softmax(dim=-1)
         v3 = self.dropout(v2)
         return v3.mul(query).norm()


# Initializing the model
n  = 8 # Number of heads in the model
m  = Model(n)
 
# Inputs to the model
a_query, a_key  = torch.randn(16 * n, 500), torch.randn(24 * n, 500)


