
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att  = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        o, s1, s2  = self.att(q1, k1, v1) 
        return o


# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(30, 640, 768)
k1  = torch.randn(250, 768)
v1  = torch.randn(250, 768)


# Outputs from the model
__output__  = m(q1, k1, v1)