
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        v3 = relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
other  = torch.tensor([5, 0]) # Please initialize 'other' as a tensor with shape (2, )
x1     = torch.randn(2, 3, 64, 64)
