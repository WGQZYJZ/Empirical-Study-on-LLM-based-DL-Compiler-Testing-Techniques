
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        v1  = torch.mm(x1,y1) + z1 
        return torch.mm(v1 ,w1)


# Initializing the model and setting parameters
m  = Model()
for n in m.parameters():
    print(n.shape) 
    n.requires_grad_(False)

m2 = Model() # Set parameters to be False by default
for n in m2.parameters(): 
    print(n.shape)  
    n.requires_grad_(True)


# Inputs to the model, same as the model in the previous task.
x1  = torch.randn(1,365,4096)
y1  = torch.randn(1,365,4096)
z1  = torch.randn(1,365,4096)
w1  = torch.randn(370,4096)


__output__  = m(x1 ,y1, z1, w1) 

