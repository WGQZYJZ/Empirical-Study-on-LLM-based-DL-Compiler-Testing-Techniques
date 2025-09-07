
class Model(torch.nn.Module):
    def __init__(self, shape1=[4], shape2=[3]):
        super().__init__()
        self.mm = torch.nn.Linear(shape1[0]*shape2[0], 5)
 
    def forward(self, x1, x2):
        v1  = self.mm(torch.cat([x1[:, None,:], x2[:, None,:]], axis=1).reshape(-1)) 
        return v1

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(5, 4)
x2 = torch.randn(5, 3)
__output__  = m(x1[:, None,:], x2[:, None,:])

|end_of_model|
|end_of_text|