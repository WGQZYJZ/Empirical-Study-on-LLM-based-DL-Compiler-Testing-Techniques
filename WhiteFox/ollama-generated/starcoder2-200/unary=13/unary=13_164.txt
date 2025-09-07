
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(832*64, 7)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) 
        v2 = torch.sigmoid(v1).clamp(min=0., max=1.)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
__input_tensor__  = torch.randn(64, 832)
 
