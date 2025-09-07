
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 8)
 
    def forward(self, x2):
        v1  = self.linear(x2)
        v2  = v1 > 0
        v3  = -0.5 * v1 # negative_slope is -0.5 in this model, you should choose any other value for the slope
        v4  = torch.where(v2, v1, v3)#torch.where returns a tensor where each element of the condition argument is True or False depending on whether its corresponding element from values is True or False.
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x2  = torch.randn(1, 10) # a vector with shape (1,)
__output__  = m(x2)
