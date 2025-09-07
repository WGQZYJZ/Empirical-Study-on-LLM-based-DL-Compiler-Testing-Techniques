
class Model(torch.nn.Module):
    def __init__(self, dim=10):
        super().__init__()
 
    def forward(self, x1):
        m1  = torch.randn([5,4])
        m2  = torch.randn([3,7,6])
 
        v1  = torch.addmm(x1, m1, m2) # Perform a matrix multiplication between matrices and add it to the input tensor.
        v2  = torch.cat((v1), dim=dim) 
        return v2

# Initializing the model
m  = Model()

