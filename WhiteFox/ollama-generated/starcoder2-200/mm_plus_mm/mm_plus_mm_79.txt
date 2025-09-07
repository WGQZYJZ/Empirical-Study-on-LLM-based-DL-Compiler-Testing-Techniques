
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v3 = torch.mm(x1,y1)  # Matrix multiplication between input1 and input2
        return v3

