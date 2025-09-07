
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v1 * v2


# Initializing the model
m  = Model()
 
# Inputs to the model 
__input1__= np.random.rand(30, 28*28).astype('float64')
__input2__ = np.random.rand(5, 10)
x1  = torch.from_numpy(__input1__)
x2  = torch.from_numpy(__input2__)
 
# Initializing the model
m(torch.randn((30, 784)))