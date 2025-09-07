
class Model(torch.nn.Module):
    def __init__(self, embed_dim=512, num_heads=8, dim_feedforward=2048):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dim_feedforward = dim_feedforward

        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads)  # Multi-head attention mechanism
        self.mlp = torch.nn.Linear(self.dim_feedforward, embed_dim)  # Feed forward network for computing the residual
        self.fc1 = torch.nn.Linear(embed_dim, self.num_heads * embed_dim)  # The main linear layer for computing attention weights

    def forward(self, x):
        # (batch size, seq length, embedding dim)

        q = self.fc1(x).contiguous().view(-1, self.num_heads, self.embed_dim)  # Compute the query
        k = torch.tanh(q)  # Apply Tanh to the query

        v = torch.tanh(k)  # Apply Tanh to the key

        x = self.attn(x, x, x)[0]  # (batch size, seq length, embedding dim)
        residual = x  # Keep a copy of the input tensor for the feed forward layer
        x = torch.nn.functional.dropout(x, p=self.dropout_p)  # Apply dropout

        h = self.mlp(x).contiguous().view(-1, self.embed_dim)  # Compute the value
        y = self.fc1(h)  # Compute the output (feed forward network)

        return y


# Initializing the model
m = Model()


