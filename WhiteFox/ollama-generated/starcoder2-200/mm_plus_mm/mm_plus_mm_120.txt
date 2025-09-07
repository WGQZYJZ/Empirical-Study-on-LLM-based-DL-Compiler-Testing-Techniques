
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
    
    def forward(self, x1, y2):
        v1  = self.mm(x1, y2) # Matrix multiplication between input1 and input2
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(5,3)
y1 = torch.randn(3, 7)
