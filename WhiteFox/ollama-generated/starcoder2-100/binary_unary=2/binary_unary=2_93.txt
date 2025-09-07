
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other 
        v4  = torch.relu(v2) # <|error|>
        return v6


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(8,3,3,3) # A random 8 x 3 x 3 x 3 tensor. Please make sure that it is not the same with "x1" from the previous task (Task 2) or "v4" of Task 1.
__output__  = m(other)

