
class Model(torch.nn.Module):
    def __init__(self, c1=50):
        super().__init__()

        self.linear = torch.nn.Linear(4 * 4 * 8, 2)
 
    def forward(self, x1, x3, x4):
        v1  = torch.mm(x1, x3) + torch.mm(x4, x3)
        return torch.relu(v1).mm(self.linear(v1))


# Initializing the model
m  = Model() 

# Inputs to the model (input1 and input2 are inputs to model m, and so on for each line of code)
x1  = torch.randn(32000, 50)
x3  = torch.rand(32000, 4 * 4 * 8)
x4  = torch.rand(32000, 4 * 4 * 8)

__output__  = m(x1, x3, x4)
