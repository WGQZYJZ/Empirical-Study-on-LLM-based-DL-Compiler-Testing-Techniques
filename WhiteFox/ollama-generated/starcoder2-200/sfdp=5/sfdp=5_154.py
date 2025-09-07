
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.softmax(x1  + 1., dim=0)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__input_tensor__  = torch.randn(512, 4608) 

