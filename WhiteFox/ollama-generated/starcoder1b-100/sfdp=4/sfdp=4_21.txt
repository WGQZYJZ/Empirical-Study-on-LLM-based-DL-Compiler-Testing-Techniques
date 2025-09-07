
class Model(torch.nn.Module):
    def __init__(self, n_heads=8, d_k=32, d_v=1024, d_ff=512, n_layers=6, dim=256, mlp_dropout=0.1):
        super().__init__()
        self.n_heads = n_heads
        self.d_k = d_k
        self.d_v = d_v
        self.dim = dim
        self.mlp_dropout = mlp_dropout
        self.positionwise_feedforward = torch.nn.Sequential(
            torch.nn.Linear(self.dim, 3 * self.n_heads * d_k),
            torch.nn.ReLU(),
            torch.nn.Dropout(mlp_dropout),
            torch.nn.Linear(3 * self.n_heads * d_k, 3 * self.n_heads * d_v),
            torch.nn.ReLU(),
            torch.nn.Dropout(mlp_dropout),
        )
 
        self.scale = 1 / math.sqrt(self.dim)
        self.pos_emb = nn.Embedding(
            int(max_len + 2 * padding), self.n_heads, embedding_dim=d_k)
 
    def forward(self, x):
        batch_size, seq_len, dim = x.shape
        qkv = self.positionwise_feedforward(x).reshape(-1, int(batch_size * 2 / math.sqrt(dim))), dim)  # Transpose and flatten the query, key, value tensors
        pos = torch.arange(0, seq_len).unsqueeze(0).expand_as(qkv) * self.scale
        attn = (qkv @ self.pos_emb(pos)) / math.sqrt(self.dim)
        attn  # Add the attention weights to the output of the positionwise feedforward
        return attn
 
 
