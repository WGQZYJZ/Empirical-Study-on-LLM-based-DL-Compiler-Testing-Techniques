

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, y1, x2, y2):
        v1 = torch.mm(x1, y1) 
        v2 = torch.mm(x2, y2)
        return v1 + v2


m  = Model()
x1 = torch.rand(30720, 5) # Randomly generated 30720 by 5 matrix of floats 32-bit 
y1 = torch.rand(48, 5)    # Randomly generated 48 by 5 matrix of floats 32-bit 
x2 = torch.rand(30720, 6) # Randomly generated 30720 by 6 matrix of floats 32-bit 
y2 = torch.rand(48, 6)    # Randomly generated 48 by 5 matrix of floats 32-bit 

