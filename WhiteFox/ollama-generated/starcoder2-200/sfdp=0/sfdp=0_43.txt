
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(32768, 5)
 
    def forward(self, x):
        sdp = torch.matmul(x, x.transpose(-2,-1))/torch.sqrt(1024.)
        aw = sdp.softmax(dim=-1)
        o = aw*aw*aw
        return o

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(8,32768)
