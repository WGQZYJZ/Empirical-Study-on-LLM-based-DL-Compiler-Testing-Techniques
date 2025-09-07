
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1 = torch.mm(x1, y2)  # Matrix multiplication of the first input tensor with the second one.
        v2 = torch.cat([v1], dim=0)  # Concatenation along dimension 0.
        return v2
 
# Initializing model
m  = Model()

