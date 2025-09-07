
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        t  = torch.mm(x1,y1) # Matrix multiplication between input1 and input2
        return t

# Initializing the model
m  = Model()

# Inputs to the model
x1  = np.random.rand(3072,512).astype(np.float64) # Input1  # Input1
y1  = np.random.rand(512 ,9 ).astype(np.float64)# Input2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.from_numpy(x1)
y1  = torch.from_numpy(y1)
 
 
