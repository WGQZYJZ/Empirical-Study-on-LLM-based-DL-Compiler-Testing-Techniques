
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(3, 5)

    def forward(self, x1):
        qk = self.query(x1) @ self.key(x1).transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        v  = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(v, dropout_p, True) # Apply dropout to the softmax output
        value = torch.matmul(attn_weight, self.value(x1)) # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
