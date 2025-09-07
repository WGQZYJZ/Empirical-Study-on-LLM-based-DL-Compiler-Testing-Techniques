
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.sigmoid(x) # Apply sigmoid to the input tensor
        return v1
 
m  = Model()


__output__  = m(torch.randn(2))