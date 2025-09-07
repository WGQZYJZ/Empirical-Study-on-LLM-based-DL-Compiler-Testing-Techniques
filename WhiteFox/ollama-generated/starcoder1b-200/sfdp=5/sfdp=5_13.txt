
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(7, 4)
 
    def forward(self, x1, x2, dropout_p=0.5):
        v1 = self.attn(x1).contiguous()
        v2 = torch.cat([x2[:, :], x2[:, :, :-1]], dim=-1) * math.sqrt(10. / 7.)
        v3 = self.attn(v2) + torch.rand_like(x2, dtype=torch.float) > 0.98 # Add a small amount of randomness to the input
        v4 = torch.dropout(v3, dropout_p, True)
        return x1 @ v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 7, 64, 64)
x2 = torch.randn(10, 4, 64, 64)
