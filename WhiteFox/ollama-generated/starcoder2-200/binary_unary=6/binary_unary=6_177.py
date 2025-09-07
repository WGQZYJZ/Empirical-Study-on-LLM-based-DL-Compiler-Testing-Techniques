
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 5)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = self.linear2(v1 - other) 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(4, 3) # a randomly generated 5-dimensional vector/tensor with size 3 * 4
__output__  = m(x1)