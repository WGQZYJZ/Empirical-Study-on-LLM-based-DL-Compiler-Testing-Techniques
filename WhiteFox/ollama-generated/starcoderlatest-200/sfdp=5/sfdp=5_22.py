
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_norm = torch.nn.LayerNorm(3, eps=1e-6)
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=4, dropout=0.1)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + torch.eye(key.shape[0]).unsqueeze(0).repeat([query.shape[0], 1, 1]) * (-2 ** 32) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        out = attn_weight @ value # Compute the dot product of the dropout output and the value
        attn_output = self.attn_norm(torch.cat((query, key, out), dim=-1))
        return attn_output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(16, 3, 128, 128)
attn_output = m(x1, x1, x1)


