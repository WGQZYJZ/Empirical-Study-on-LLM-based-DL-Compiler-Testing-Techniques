
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 2)
        self.key = torch.nn.Linear(3, 2)
 
    def forward(self, x1, x2, attn_mask=None):
        q  = self.query(x1)
        k  = self.key(x2)
        v  = torch.einsum('bi,bj->bij', (q, k)) * math.sqrt((q.size(-1), k.size(-1)))
        if attn_mask is None:
            attn_weight = torch.softmax(v, dim=-1)
            output  = attn_weight @ x2
            return output
        else:
            attn_weight = torch.softmax(v * attn_mask, dim=-1)
            output  = (attn_weight @ x2 + attn_weight).div(1 - attn_mask)
            return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 2, 64, 64)
