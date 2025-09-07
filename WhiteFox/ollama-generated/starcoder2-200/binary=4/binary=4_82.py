
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1 + other


# Initializing the model
m2 = Model()

# Input to the model 
other = torch.zeros_like(v1) # Creating a zero tensor of similar shape as the output of the previous model with the same device and dtype, for example: v1 = torch.randn(50).cuda(), other = torch.zeros_like(v1)
x2 =  torch.randn((3,)) # Sample input to the model 
x2 = x2.view(-1, 3 * 4).to('cpu')
x2 = torch.tensor(x2).to('cpu',dtype=torch.float64)

 