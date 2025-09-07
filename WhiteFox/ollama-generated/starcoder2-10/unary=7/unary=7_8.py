
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Linear(3,8)
        self.conv2 = torch.nn.ELU()
 
    def forward(self, x1):
        v1  = self.conv1(x1) + 3 # linear transformation + 3
        v4 = v1 * torch.clamp(min=0, max=6, input=v1) 
        v2 = v4 / 5 # division by 5
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)
