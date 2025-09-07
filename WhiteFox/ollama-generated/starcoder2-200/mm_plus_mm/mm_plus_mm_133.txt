

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1 = torch.mm(x1,y1)
        v2  = torch.mm(v1,x2) + torch.mm(v1,y2)
        return v2

m = Model()

# Input tensors to the model