
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t1  = torch.rand(2)
         t2  = t1 + t1[None]
         v3  = self.linear(t2)
# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(4, 5)
