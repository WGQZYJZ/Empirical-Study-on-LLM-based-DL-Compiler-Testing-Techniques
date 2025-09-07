
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # Pass another tensor to the addition operation
        v3  = F.relu(v2) 
        return v3

# Initializing the model with an argument
other  = torch.randn(5, 784)
m  = Model()


# Inputs to the model
x1  = torch.randn(600, 5)
__output__  = m(x1)
