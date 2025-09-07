
class Model(torch.nn.Module):
    def __init__(self, n1, n2):
        super().__init__()
        self.matmult  = torch.nn.Linear(n1*n2, n1+n2)
 
    def forward(self, x1, x2, x3, x4): 
        v1  = self.matmult(torch.cat([x1.reshape(-1),
                                      x2.reshape(-1)], dim=0))
        v2  = torch.mm(v1[:,None],
                       (x3+x4).reshape(-1, None)).reshape(x1.shape)
        return v2

# Initializing the model with specified sizes of input tensors
m  = Model(n1=64, n2=96)

 # Inputs to the model
x1 = torch.randn(30, 587)
x2 = torch.randn(30, 1)
x3 = torch.randn(30, 64*96).reshape(30, 64, 96) # This is the output tensor from the previous model layer!
x4 = torch.randn(30, 128).reshape(30, 1, 128) # This is the output tensor from the previous model layer!
