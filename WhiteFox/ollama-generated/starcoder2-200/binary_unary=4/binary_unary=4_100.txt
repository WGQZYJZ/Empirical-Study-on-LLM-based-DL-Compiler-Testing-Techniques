
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1, y2):
        v1 = self.linear(x1)
        v2 = v1 + y2
        v3 = F.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(5, 8)
y2  = torch.randn(7, 9) # In this example we use 0 tensor, but it is ok if you have another tensor here.
__output__  = m(x1, y2)

