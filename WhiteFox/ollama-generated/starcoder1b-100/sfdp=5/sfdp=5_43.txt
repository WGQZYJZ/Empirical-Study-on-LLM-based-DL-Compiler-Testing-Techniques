
class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.attn = torch.nn.Linear(dim, dim)

    def forward(self, x1, x2):
        qk = torch.einsum('ij,i->j', x1, x2) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += self.attn(None) * 0.000001 # Add an attention mask to the scaled dot product

        attn_weight = F.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = F.dropout(attn_weight, p=self.dropout_p, training=training) # Apply dropout to the softmax output
        v  = torch.einsum('ij,j->i', attn_weight, x2) # Compute the dot product of the dropout output and the value

        return v


# Initializing the model
m = Model(dim=128)
x1  = torch.randn(4, 64, 128)
x2  = torch.randn(4, 3, 128)
