
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 13)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation
        v3 = F.relu(v2)
        return v3

# Initializing the model with some random parameters
m  = Model()
__parameters_ = m.parameters()
for param in __parameters_:
    param.data.normal_(0,1)

 # Inputs to the model for a forward pass 
 x1  = torch.randn(256, 3784)
 
 # Running a forward pass through our model
 