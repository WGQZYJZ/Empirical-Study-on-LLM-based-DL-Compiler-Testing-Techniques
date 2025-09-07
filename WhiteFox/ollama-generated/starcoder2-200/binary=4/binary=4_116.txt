
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1): 
        v1 = self.linear(x1) + 0.836779 # add another tensor to the output of a linear transformation
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 512)
__output__  = m(x1)