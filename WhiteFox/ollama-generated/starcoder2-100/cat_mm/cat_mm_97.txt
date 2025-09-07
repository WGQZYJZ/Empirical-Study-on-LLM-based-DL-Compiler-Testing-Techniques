
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat = torch.nn.Linear(128, 40)
 
    def forward(self, x1):
        v1  =  torch.mm(x1, x1) 
        v2  =  torch.cat([v1 for i in range(7)]) 
        return v2
# Initializing the model
m = Model()


# Inputs to the model
i1  = torch.randn(4096, 32, 8)  # First input tensor of the model (of size: [batch_size x 32x 8])
i2  = torch.randn(4096, 8)       # Second input tensor of the model (of size: [batch_size x 16])


__output__  = m(torch.randn(32, 32))

The generated model example contains a public API call, which is different from previous one.