
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        self.scale = torch.randn(q1) # random
        # ......
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
q1  = torch.randn(4, 3072)
k1  = torch.randn(8, 65536)
v1  = torch.randn(8, 3072)
 
__output__  = m(q1, k1, v1)

