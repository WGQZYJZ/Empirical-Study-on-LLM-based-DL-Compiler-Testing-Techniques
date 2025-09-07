
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x): 
        y  = self.linear(x)
        return y - y


# Initializing the model
m2  = Model()


# Inputs to the model
x   = torch.randn(4096,)
x1  = torch.randn(4096,512).to('cuda')
x2  = torch.randn(1)
__output_model2__ = m2(x2)

