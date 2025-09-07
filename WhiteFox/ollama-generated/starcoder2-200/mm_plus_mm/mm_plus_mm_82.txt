
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1, z1, w1):
        m1 = torch.mm(x1, y1)
        m2 = torch.mm(z1, w1) 
        v1  = m1 + m2
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model 
input1 = torch.randn((3075, 8))  
input2 = torch.randn(3964, 8) 

input3 = torch.randn((3075, 1))
input4 = torch.randn(1982, 1)

output1  = m(input1, input2, input3, input4)

 # Output of the model 
