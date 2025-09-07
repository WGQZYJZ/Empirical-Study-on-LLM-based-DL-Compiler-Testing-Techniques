
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3, 8)
        self.sig  = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v2 = self.sig(x1 * self.conv())
        return v2

m  = Model()

 # Initializing the model
m0 = Model()
x1 = m0(torch.randn(1,3))

__output__= m(x1)
