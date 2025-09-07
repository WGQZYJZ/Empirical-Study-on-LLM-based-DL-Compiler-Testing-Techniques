
class Model(torch.nn.Module):
    def __init__(self, dim1=0):
        super().__init__()
 
    def forward(self, x): 
        m1 = torch.randn([256, 48])
        m2 = torch.randn([48, 9273])
 
        v1 = torch.addmm(x, m1, m2)
        
        v2 = torch.cat((v1,), dim1) # <-- This is a concatenation operation!

        return v2

# Initializing the model
m = Model()


# Inputs to the model
dim  = random.randint(0, 3)
x   = torch.randn([8,48])
__output__  = m(x)