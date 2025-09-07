
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.w_proj = torch.nn.Linear(d_model, 8)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        value  = torch.matmul(attn_weight, x2)  # Compute the dot product of the dropout output and the value
        return self.w_proj(value)


# Initializing the model
m = Model()
m.train()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
