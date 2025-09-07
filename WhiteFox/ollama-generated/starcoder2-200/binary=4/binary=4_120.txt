
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*3, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
-      v2  = v1 + torch.randn_like(v1) # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.rand(8,3*32*32)
