
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim)
        self.key = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
 
    def forward(self, x1, x2):
        qk = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ self.value(x2)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model(dim=64)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
