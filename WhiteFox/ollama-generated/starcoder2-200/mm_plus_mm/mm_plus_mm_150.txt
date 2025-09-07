
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1  = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        v3  = torch.mm(x2,y2)# Matrix multiplication between input3 and input4
        return (v1 + v3).max()

# Initializing the model
m  = Model()

# Inputs to the model
a  = torch.randn(76800) # First input with shape of [batch_size*rows]
b  = a[torch.randperm(len(a))].reshape([25, 49])
c  = torch.randn(4143) # Second input with shape of [rows*cols]
d  = c[torch.randperm(len(c))].reshape([70, 68]).t()
__output__  = m(a, b, c , d).detach().numpy()

