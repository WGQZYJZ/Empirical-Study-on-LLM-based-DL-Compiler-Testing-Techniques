
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 3072) # input size: (batch_size, length, hidden_dim) * (batch_size, hidden_dim, key_length) / (batch_size, hidden_dim, value_length) = output size: (batch_size, length, hidden_dim, key_length)
        self.attn = torch.nn.MultiheadAttention(16, 24, dropout=0.5) # input shape: (seq_len, batch_size, embed_dim), num heads: 8, output shape: (seq_len, batch_size, embed_dim * 3)
        self.linear2 = torch.nn.Linear(10752, 768) # input size: (batch_size, seq_len, embed_dim * 4), output size: (batch_size, seq_len, hidden_dim)
 
    def forward(self, x):
        batch_size = x.shape[1]
        length = x.shape[0]

        v1  = self.linear1(x).view(batch_size, -1, x.shape[-1])
        v2 = torch.transpose(v1, 1, 2) # Transpose the second and third dimensions for the multihead attention layer, (batch_size * hidden_dim, embed_dim * 4)
        v3, _ = self.attn(v1, v2, v1) # Multi-Head Attention
        return self.linear2(v3.view(batch_size, length, -1))


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10, 64, 768) # (seq_len, batch_size, hidden_dim) -> (batch_size * seq_len, hidden_dim)
