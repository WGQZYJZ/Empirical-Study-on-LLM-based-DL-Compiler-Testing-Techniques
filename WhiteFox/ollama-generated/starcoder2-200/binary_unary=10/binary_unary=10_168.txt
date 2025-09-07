
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024*3*3, 5)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(batchsize, 1024*3*3).to("cuda") + \
               torch.randn(5).to("cuda") * 2 - 1
__output__   = m(input_tensor)

