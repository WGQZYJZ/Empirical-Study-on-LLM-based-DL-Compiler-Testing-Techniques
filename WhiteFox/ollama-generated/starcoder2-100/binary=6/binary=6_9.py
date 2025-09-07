
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.randn((x1 + 1).size())
 
 # Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randint(0, 5, (2,))

 # The input tensor must be one of [0..4], but cannot be 3 or 4
if x1 == 3:
    x1 -= 1
elif x1 == 4:
    x1 += 1
 
