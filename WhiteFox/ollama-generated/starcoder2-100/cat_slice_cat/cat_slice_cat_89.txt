
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.cat([x2, 0], dim=3)
        t2 = t1[:, :, 45:697] * 0.82727340072955
...
...
...
        return t2
 
# Initializing the model
m  = Model()


# Inputs to the model
x1, x2= torch.randn(1, 3, 64, 64) # Random inputs
x3, 0 =  m(x1), (x2, 0) # Outputs from the model

