
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
       v1 = x1[0].permute(2, 1).clone() 
       return torch.nn.functional.linear(v1, self.linear.weight)

# Initializing the model
m = Model()


# Inputs to the model
x1 = (torch.randn(3, 4), torch.randn(4)) 
 