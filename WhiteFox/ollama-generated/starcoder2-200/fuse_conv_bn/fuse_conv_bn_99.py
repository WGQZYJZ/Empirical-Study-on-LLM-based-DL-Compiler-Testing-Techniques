
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv2d(3, 3, 5) 
        bn    = torch.nn.BatchNorm2d(3)    
        v     = conv(x1)
        output= torch.nn.functional.batch_norm(v, conv.running_mean, conv.running_var, conv.weight, conv.bias)
        return x


# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(1,3,28,28)
__output__  = m(x1)

