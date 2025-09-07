
class SelfAttnModel(torch.nn.Module):
    def __init__(self, embedding_dim=128):
        super().__init__()
        self.linear = torch.nn.Linear(embedding_dim, embedding_dim)
 
    def forward(self, x1, x2):
        qk  = self.linear(x1) @ self.linear(x2).transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return self.linear(attn_weight * x2) + x1


# Initializing the model
m = SelfAttnModel()

# Inputs to the model
x1 = torch.randn(1, embedding_dim, query_len, key_len)  # The query tensor
x2 = torch.randn(1, embedding_dim, query_len, value_len)  # The key tensor
