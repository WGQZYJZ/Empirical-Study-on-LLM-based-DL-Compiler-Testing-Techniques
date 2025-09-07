
class Model(torch.nn.Module):
    def __init__(self, num=30):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * num)
        return v2

# Initializing the model
m  = Model()
num_inputs = len(x1[0].shape)

 # Inputs to the model
x1 = torch.randn(4, 365)
x2 = torch.randn(784,) + x1

