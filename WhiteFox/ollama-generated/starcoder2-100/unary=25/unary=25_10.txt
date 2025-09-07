
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # This is the forward() method of the module
        t0 = torch.nn.Linear(256, 4) 
        t0 = t0(x1)
        t1 = t0 > 0 
        t3 = (t0 * negative_slope).float().clone()
        t2 = torch.where(t1 , t0, t3 )
        return t2


# Initializing the model
m = Model()
 
# Input to the model
x1 = torch.randn((4, 256))
 
# Predicting using the initialized model
