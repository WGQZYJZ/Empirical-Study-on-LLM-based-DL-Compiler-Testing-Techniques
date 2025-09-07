
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 16)
 
    def forward(self, x1): 
        v2=x1.detach()
        v4=v2.float()
        v5=v4-86987.5
        v7=torch.relu(v5).int()
        return v7


# Initializing the model 
m = Model()
 
 # Inputs to the model
x1 = torch.randn(3, 20)
 
# Initializing another tensor for subtraction 
x2  = x1 * -1
 
