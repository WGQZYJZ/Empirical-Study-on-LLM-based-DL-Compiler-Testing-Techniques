
class Model(torch.nn.Module):
    def __init__(self, dim, heads=8, dropout_p=0):
        super().__init__()
        self.dim = dim
        self.heads = heads
        self.dropout_p = dropout_p
        
        self.attn = torch.nn.MultiheadAttention(
            dim=dim,
            num_heads=heads)
        
        self.fc1 = nn.Linear(self.dim * 2, self.dim)
        self.fc2 = nn.Linear(self.dim, 1)

    def forward(self, x):
        # (batch_size, seq_len, dim)
        query = x[:, :, : self.dim // 2]
        key   = x[:, :, self.dim // 2:]
        
        # compute attention
        attn = self.attn(query, key, value=key)
        # attn: (batch_size, seq_len, seq_len)

        # dropout
        attn = torch.dropout(attn, p=self.dropout_p, training=training)
        # attn: (batch_size, seq_len, seq_len)
        
        # compute value
        query  = attn @ key.transpose(-2, -1)  # (batch_size, seq_len, dim // 2)
        output = torch.sigmoid(self.fc1(torch.cat((query, key), dim=-1))) * 0.5
        return self.fc2(output)


# Initializing the model
m = Model()

