

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        v1  = torch.addmm(x1)  # A matrix multiplication and addition operation on input tensor
        v2  = torch.cat([v1], 0) 
        return v2

# Initializing the model
m = Model()


