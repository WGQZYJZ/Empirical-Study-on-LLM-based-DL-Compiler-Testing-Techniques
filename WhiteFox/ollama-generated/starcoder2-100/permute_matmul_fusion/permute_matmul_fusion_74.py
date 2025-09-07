
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       t2 = x1.permute([0, 3]).reshape((x1.shape[0], -1)) 
       t1 = torch.matmul(t2, t2)
       t1 += torch.eye(x1.size()[0])
       return t1


# Initializing the model
m = Model()
# Inputs to the model
x1  = torch.randn((32, 784))
