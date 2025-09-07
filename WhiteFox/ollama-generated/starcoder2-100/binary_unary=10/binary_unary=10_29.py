
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
        self.other = torch.randn([32]).abs()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model 
__inputs__  = (torch.randn([32,784]),)
 
