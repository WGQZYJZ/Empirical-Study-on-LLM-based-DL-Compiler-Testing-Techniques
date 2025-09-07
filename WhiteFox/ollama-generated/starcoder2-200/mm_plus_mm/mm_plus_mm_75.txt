
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v0  = torch.mm(x1, x2)
        v1  = torch.mm(x3, x4)
        return v0 + v1

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(512, 68 * 79)
 x2  = torch.randn(512, 68 * 79)
 x3  = torch.randn(504, 68* 79)
 x4  = torch.randn(504, 68* 79)
  