
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = v0 - other_value
        v2 = F.relu(v1)
        return v2


m  = Model()

# Initializing the model
m  = Model()
other_value  = torch.randn([]) # Value that you will subtract from the output of the linear transformation
 

# Inputs to the model
x1  = torch.randn(3, 16)


# Output after execution
