
class Attention(torch.nn.Module):
    def __init__(self, inv_scale=1., nhead=8):
        super().__init__()
 
        self.query = torch.nn.Linear(embed_dim, embed_dim)
        self.key = torch.nn.Linear(embed_dim, embed_dim)
        self.value = torch.nn.Linear(embed_dim, embed_dim)
 
        self.scale  = inv_scale ** -0.5
 
    def forward(self, query=None):
        k1  = self.query(query)
        k2  = self.key(k1)
        v1  = self.value(k1)
        v2  = self.value(v1)
 
        scaled_dot_product  = torch.matmul(k1, k2.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v2)
# Initializing the model
model = Attention()

# Inputs to the model
query = torch.randn([3, 8, 56, 56])
 
