
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2, x3):
        kq  = torch.matmul(x1, x2) / math.sqrt(x1.size(-1))
        kq = kq + torch.ones_like(qk) * (1 - torch.eye(x1.shape[-1]))
        attn_weight  = torch.softmax(kq, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)
        value  = torch.matmul(attn_weight, x3)
        return value


# Initializing the model
m = Model()

