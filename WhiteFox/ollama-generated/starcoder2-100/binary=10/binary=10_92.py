
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 3)
 
    def forward(self, x2):
        v754 = self.linear1(x2) 
        v1906 = v754 + torch.randn_like(v754)
        return v1906


# Initializing the model
m  = Model()

# Inputs to the model
x3  = torch.randn(1,8,128,128)

