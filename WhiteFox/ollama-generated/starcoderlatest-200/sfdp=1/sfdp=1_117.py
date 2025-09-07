
class Model(torch.nn.Module):
    def __init__(self, num_queries: int = 4096, qkdim: int = 128, dropout_p: float = 0.5):
        super().__init__()
        self.num_heads = num_heads # Number of attention heads in the MultiHeadAttention module
        self.scale = scale 
        self.attention = torch.nn.MultiheadAttention(
            num_heads=self.num_heads,
            embed_dim=qkdim, # Embedding dimension in the MultiHeadAttention module
            dropout=dropout_p,
        )
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        qk = self.attention(query, key, value)[0]  # Compute attention on the query, key, and value tensors using MultiHeadAttention module
        return qk


# Inputs to the model
q1 = torch.randn(3, 8, 512)
k1 = torch.randn(3, 8, 64)
v1 = torch.randn(3, 8, 512)
