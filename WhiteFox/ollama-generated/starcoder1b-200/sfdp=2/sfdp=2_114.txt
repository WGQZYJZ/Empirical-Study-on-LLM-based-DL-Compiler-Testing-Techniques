
class Model(torch.nn.Module):
    def __init__(self, embed_dim=100, num_head=3):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_head = num_head
 
        self.layer_norm1 = torch.nn.LayerNorm(embed_dim)
        self.layer_norm2 = torch.nn.LayerNorm(embed_dim)
 
        self.attention  = self._make_ffn(embed_dim=embed_dim,
                                          hidden_size=embed_dim // num_head,
                                          dropout_p=dropout_p)
 
    def _make_ffn(self, embed_dim, hidden_size, dropout_p):
        m = torch.nn.ModuleList([
            torch.nn.Linear(embed_dim, hidden_size),  # Linear projection
            torch.nn.GELU(),                      # Generalized Linear Unit (GLU)
            torch.nn.Linear(hidden_size, embed_dim) # Linear projection back
        ])
 
        m[0].bias = None
 
        m[-1].bias = None
        return nn.Sequential(*m)
 
    def forward(self, x1):
        q  = self.embed_dim + self.num_head * self.embed_dim
        k  = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of each vector independently
        k = k / math.sqrt(self.embed_dim) # Scale by sqrt(d_k) (batch size, max attention head width)
        k = k.softmax(-1)   # Apply softmax to the scaled dot product
 
        v  = self._make_ffn(embed_dim=self.embed_dim, hidden_size=self.embed_dim // self.num_head, dropout_p=dropout_p)(k)
        v *= k  # Scale the dot product by k
 
        x2 = torch.matmul(x1, v) # Compute the sum of the products of two vectors
        x3 = torch.nn.functional.layer_norm(x2 + self.embed_dim * k, elementwise_affine=True) # Add the projection to the attention score (batch size, max attention head width)
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(10, 64, 256, 256)
