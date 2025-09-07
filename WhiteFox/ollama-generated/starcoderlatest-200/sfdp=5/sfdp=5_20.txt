
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key   = torch.nn.Linear(3, 8)
 
    def forward(self, q1, k1):
        v1 = self.query(q1) @ self.key(k1).transpose(-2, -1) / math.sqrt(v1.size(-1))
        attn_weight = torch.softmax(v1, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ self.value
        return output

# Initializing the model
m = Model()
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
