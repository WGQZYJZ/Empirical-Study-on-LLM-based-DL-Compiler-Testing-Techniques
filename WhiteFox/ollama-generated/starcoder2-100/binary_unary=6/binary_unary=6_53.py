
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4,8)
        self.relu  = torch.nn.ReLU()
        self.linear2  = torch.nn.Linear(8,4)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 - other_val  # Subtract 'other' from the output of the linear transformation
        
        return v2

# Initializing the model and setting 'other' to a constant value `0.3`
m  = Model()
other_val = torch.tensor(0.3)


# Inputs to the model: a random tensor with 4 dimensions, each dimension size 8.
x1  = torch.randn(256, 4 ,8 ,8 )
__output__  = m(x1)

