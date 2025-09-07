
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None, input3=None, input4=None):
        super().__init__()
 
    def forward(self, t1):
        t2  = torch.mm(t1[0], t1[1])
        t3  = torch.mm(t1[2], t1[3])
        t5  = t2 + t3
 
        return t5

# Initializing the model and setting its input values as well
t1  = torch.randn(4, 6)
m   = Model()
