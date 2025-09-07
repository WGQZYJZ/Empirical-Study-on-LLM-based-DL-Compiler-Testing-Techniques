
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 512)
        self.linear2 = torch.nn.Linear(512, 256)
        self.linear3 = torch.nn.Linear(256, 128)
 
    def forward(self, x):
        t1 = torch.mm(x, x) # Matrix multiplication between the input and itself
        t2 = torch.mm(x, x)
        t3 = t1 + t2
        return t3
 
# Initializing the model
m = Model()
 
 # Inputs to the model
 x  = torch.randn(2, 2048)
 