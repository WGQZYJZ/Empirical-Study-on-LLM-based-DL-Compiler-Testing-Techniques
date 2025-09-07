
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(40, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2, attn_mask=None):
        v1 = F.leaky_relu(self.linear1(x1), negative_slope=-0.2)
        v2 = self.linear2(v1)
        qk  = torch.matmul(v2, x2) / math.sqrt(x2.size(-1))
        attn_weight = F.softmax(qk, dim=-1) * x2
        return attn_weight @ v1


# Initializing the model
m = Model()


