
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(embed_dim=3, num_heads=2)
 
    def forward(self, query, key, value):
        v1  = self.attn(query, key)[0]
        v2  = v1 * scale_factor 
        v3  = torch.nn.functional.dropout(v2, p=dropout_p)
        return v3.matmul(value)

# Initializing the model
m  = Model()

 # Inputs to the model
 query = torch.randn(8, 16, 4)
 key   = torch.randn(8, 16, 50)
 value = torch.randn(8, 16, 3)
  __output__  = m(query, key, value)


