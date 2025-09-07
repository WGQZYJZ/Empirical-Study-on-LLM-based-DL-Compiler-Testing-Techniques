
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6,12)
 
    def forward(self, x1):
        v0  = torch.randn(5,3)#input tensors
        v0  = torch.cat((v0,torch.tensor([4.,5.], device='cuda')))
        v0  = self.linear(v0)
        v1  = v0 + other
        return v1


# Initializing the model
m  = Model()
other = torch.randn(2893)
__output__  = m(x1, other=other)

