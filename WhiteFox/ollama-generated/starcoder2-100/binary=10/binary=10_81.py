
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1) + __replace_with_your_other_tensor__
        return v1


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(1, 64)
__output__  = m(x1)