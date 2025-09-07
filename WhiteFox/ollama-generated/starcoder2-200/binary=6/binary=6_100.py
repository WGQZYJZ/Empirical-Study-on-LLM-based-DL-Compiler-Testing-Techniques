
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other # 'other' should be a constant or a tensor that is defined before the subtraction operation.
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(64, 5)
 
 
# Other data
other  = torch.tensor([3., -0.1, -0.9]) 
 
__output__  = m(x1)

