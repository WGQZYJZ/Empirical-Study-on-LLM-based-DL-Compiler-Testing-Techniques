
class Attention(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
 
        self.query = torch.nn.Linear(hidden_size, 8)
        self.key   = torch.nn.Linear(hidden_size, 16)
        self.value = torch.nn.Linear(hidden_size, 24)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):
 
        qk  = (self.query(query).transpose(-2, -1) @ self.key(key)) / math.sqrt(query.size(-1))
        qk += (attn_mask == 0)
        attn_weight  = torch.softmax(qk, dim=-1)
 
        output        = (self.value(attn_weight) @ value).to(torch.float32)
 
        return output

m = Attention()


# Initializing the model
m.eval()


x1 = torch.randn(80, 4096)
x2 = torch.randn(80, 5760)


# Outputs of the model
output1 = m(x1)


