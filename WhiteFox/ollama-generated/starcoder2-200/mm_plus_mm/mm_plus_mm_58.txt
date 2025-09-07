
class Model(torch.nn.Module):
    def __init__(self, in1):
        super().__init__()
 
    def forward(self, x1, x2):  # Note that x1 is a single 3D tensor and x2 is a 4D tensor
        v1 = torch.mm(x1, x2) + torch.mm(x2, x1) 
        return v1

# Initializing the model
m  = Model()


