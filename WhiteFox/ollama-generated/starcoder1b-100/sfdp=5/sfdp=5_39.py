
class Model(torch.nn.Module):
    def __init__(self, key_size=3, value_size=4):
        super().__init__()
        self.key_size = key_size
        self.value_size = value_size
 
    def forward(self, x1, x2):
        # (batch_size, seq_len, embed_dim)
        x1_shape = x1.shape
        batch_size, seq_len, embed_dim = x1_shape[0], x1_shape[1], x1_shape[2]
        # Compute the dot product of the query and key, and scale it.
        query = torch.mm(x1, x2) / math.sqrt(embed_dim)
        attn_mask = (query.unsqueeze(-1).expand(batch_size, seq_len, seq_len)).float()

        # Apply softmax to the result.
        qk = torch.matmul(query, x2.transpose(-2, -1)) / math.sqrt(embed_dim)
        qk = F.softmax(qk, dim=-1)
        qk = torch.dropout(qk, dropout_p, True)

        # Compute the dot product of the dropout output and the value
        out = torch.matmul(qk, x2)

        return out

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 4, 64, 64)
