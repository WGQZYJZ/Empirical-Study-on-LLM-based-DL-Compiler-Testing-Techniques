
class Attention(torch.nn.Module):
    def __init__(self, query_dim, key_dim, num_heads):
        super().__init__()
        self.query = torch.nn.Linear(query_dim, num_heads * key_dim)
 
    def forward(self, x1):
        qk  = self.query(x1).view(-1, 8, 32, -1)
        softmax_qk  = qk.softmax(dim=-1)
        output  = torch.matmul(self.value(x1), softmax_qk).squeeze(-1)
        return output
 
    def value(self, x1):
        return torch.nn.Linear(key_dim * num_heads, key_dim)(x1).view(-1, 32, -1)


# Initializing the model
m = Attention()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 32)
