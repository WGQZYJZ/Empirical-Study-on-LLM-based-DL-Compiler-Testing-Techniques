
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
        self.key = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(8, 16)
        self.attn_mask = torch.nn.Parameter(torch.randn(8))
 
    def forward(self, x):
        query  = self.query(x)  # (batch, q, num_heads, head_size)
        key    = self.key(x)    # (batch, k, num_heads, head_size)
        value  = self.value(x)   # (batch, v, num_heads, head_size)
        qk     = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn_weight = F.softmax(qk + self.attn_mask, dim=-1)  # Apply softmax to the result
        output      = torch.matmul(attn_weight, value)   # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 8, 32, 64)
