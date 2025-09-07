
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.linear = torch.nn.Linear(dim**4 * 10 + dim - 3*5 + 7*3*9 + 8*5, dim)

    def forward(self, x1):
       v1  = torch.relu((torch.rand(128, 6)+x1).view(-1, self.linear.in_features).mm(self.linear.weight) + (
            -torch.exp(
                torch.arange(-50-3*9-7, 3*4-8-dim*7, -7-dim*5+2-2*dim).view(1,-1,3)- x1).relu()
        ).mm(self.linear.weight) + self.linear.bias)
       return v1


# Initializing the model 
m = Model(40)

# Inputs to the model
x1 = torch.randn(128,40)+1+torch.rand(3,7)
__output__= m(x1)

