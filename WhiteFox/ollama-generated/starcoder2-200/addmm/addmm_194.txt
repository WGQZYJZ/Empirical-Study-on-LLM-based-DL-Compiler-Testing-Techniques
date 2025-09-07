
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, 2) + torch.randn([4500]) 
        return v1
 
# Initializing the model
m = Model()

# Inputs to the model (assuming that they are generated in a previous step)
x1 = torch.randn(100, 19367) # The first input tensor with shape of [batch_size x 19367]
inp = torch.zeros([4500]) 
 
__output__  = m(x1, inp=inp)