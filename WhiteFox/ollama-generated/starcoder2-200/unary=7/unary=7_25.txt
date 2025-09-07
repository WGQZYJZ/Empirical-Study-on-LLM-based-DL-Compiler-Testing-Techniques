
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
 
        self.fc1 = torch.nn.Linear(**kwargs["kwargs"])
 
    def forward(self, x):
        out  = self.fc1(x)
 
        if kwargs['use_relu']:
            return F.selu(out), out
        else: 
            return F.softmax(out), out


# Initializing the model
m = Model(**kwargs)
 
# Inputs to the model
inputs = torch.rand((3, 7))
__output__, out2  = m(x1)

