
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=5):
        v1 = torch.nn.Linear(3, 8)(x1)
        v2 = v1 - x2
        v3 = torch.nn.ReLU()(v2)
        return v3
 
m  = Model()
 
# Inputs to the model (Note: We're not using the input tensor x1 here. Instead we're passing an additional argument "x2=5".)
x1 = torch.randn(1, 3, 80, 80)
x2 = 4
