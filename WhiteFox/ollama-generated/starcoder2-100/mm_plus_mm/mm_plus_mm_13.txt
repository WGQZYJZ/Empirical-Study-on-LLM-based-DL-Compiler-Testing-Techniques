
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v0  = torch.mm(x1,y1) + torch.mm(x2,y2)
        return v0


# Initializing the model
m  = Model()


# Inputs to the model (in order of appearance in the forward method: [x1, y1, x2, y2])
inputs = [torch.randn(8732, 512),
          torch.randn(8732, 64), 
          torch.randn(8732, 512), 
          torch.randn(8732, 64)]


# Initializing the model
m = Model()
 
# Inputs to the model (in order of appearance in the forward method: [x1, y1])
inputs = [[torch.randn(4096)], [torch.randn(512)]]


