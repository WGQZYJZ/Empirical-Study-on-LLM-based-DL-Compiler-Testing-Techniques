
class Model(torch.nn.Module):
    def __init__(self, a1, a2, a3, a4):
        super().__init__()
        self.a1  = torch.nn.Linear(80*80*576, 9)
        self.a2  = torch.nn.Linear(256*576*320, 5)
        self.a3  = torch.nn.Linear(4*4*1024, 577) 
        self.a4  = torch.nn.Dropout()

    def forward(self, input):        
        v1  = self.a1(input).view(-1, 80, 80, 9)
        v2  = self.a2(v1).view(-1, 576*320, 4, 4)
        v3  = torch.mm(self.a3(torch.relu(v2)), input) + 1 
        return self.a4(v3)

# Initializing the model
m  = Model(torch.nn.Linear, torch.nn.Dropout, torch.nn.Dropout, torch.nn.ReLU)


# Inputs to the model
x1  = torch.randn(256*80*80*9)
x2  = torch.randn(8320*4*4*7*5)
__output__  = m(x1, x2)

