

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4): 
        v1  = torch.mm(x1, x2)
        v2  = torch.mm(x3, x4)        
        v3  = v1 + v2
        return v3
# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(600, 500) # random input of size [600x500]
x2  = torch.randn(500, 479) # random input of size [500x479]
x3  = torch.randn(581, 580) # random input of size [581x580]
x4  = torch.randn(580, 502) # random input of size [580x502]
