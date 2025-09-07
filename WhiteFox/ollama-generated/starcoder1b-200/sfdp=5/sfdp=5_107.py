
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Transformer()
 
    def forward(self, x1, x2, mask=None):
        return self.attn(x1, x2, mask)


# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(2, 3, 8, 64)
k1  = torch.randn(2, 3, 8, 64)
__output__  = m(q1, k1, mask=x1)


