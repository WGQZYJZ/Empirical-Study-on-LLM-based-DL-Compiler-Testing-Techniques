
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, t3): # Add a tensor 't3' as an input
        v1  = self.conv(x1) + other_tensor
        return v1


m  = Model()
 
x1  = torch.randn(1, 3, 64, 64)
t2 = torch.randn(8, 5) # 'other' is a tensor passed as input to the forward method
__output__  = m(x1, t3=t2)

