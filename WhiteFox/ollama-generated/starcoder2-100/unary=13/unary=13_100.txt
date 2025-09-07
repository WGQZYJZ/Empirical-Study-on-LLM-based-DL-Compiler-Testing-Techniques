
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2 
        return v3


# Initializing the model and inputs to it
m  = Model()
x1  = torch.randn(1, 32*64*64) # the input tensor to the model. The shape of this tensor is (N, 32 * 64 * 64), where N is the batch size. 

__output__  = m(x1)

