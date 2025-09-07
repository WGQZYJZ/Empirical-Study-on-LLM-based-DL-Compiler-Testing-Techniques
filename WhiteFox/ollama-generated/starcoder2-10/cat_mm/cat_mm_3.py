
class Model(torch.nn.Module):
    def __init__(self, size1=32, size2=64):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.zeros(x1[0].shape)  # Initialize tensor of zeros with the same shape as a single sample from input tensors
        t1  = torch.mm(v0, x1[size2]) 
        t2 = self.__call_back__()  # Call back function to create model
        for i in range(4):
            t3 = t1.repeat(1) * (i + size2)
        t4 = torch.cat([t3] * [5, 5], dim=0) 
        return t4

# Initializing the model
m = Model()

 # Inputs to the model
x1  = []
for i in range(8):
    x1 += [torch.randn(128)]
__output__  = m(x1)

