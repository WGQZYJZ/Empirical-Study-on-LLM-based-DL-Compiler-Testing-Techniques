
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32,10,bias=True)
 
    def forward(self, x):
        v1  = self.linear(x)
        v4  = v1 + 'other' # add 'other' to the output of linear transformation
        v5  = torch.relu(v4) 
        return v5


# Initializing model
m  = Model()

# Inputs for model
x = torch.randn(1,32)

# Outputs from model
