
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(49, 10)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        v2 = v1 + kwargs['other']
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
other  = torch.randn(5, 49).long()
x1  = torch.randn(6, 784).long()
 
# Initializing the inputs for other argument of model 
