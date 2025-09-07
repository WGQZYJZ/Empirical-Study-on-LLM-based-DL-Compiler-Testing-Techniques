
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1) 
        v2  = v1 * 0.5 # multiply_1
        v3  = torch.pow(v1, 3)# pow
        v4  = v3 * 0.044715# multiply_2
        v5  = v1 + v4  # add_1
        v6  = v5 * 0.7978845608028654  # multiply_3 
        v7  = torch.tanh(v6) # tanh
        v8  = v7 + 1# add_2
        v9  = v2 * v8# multiply_4
        return v9


# Initializing the model
m  = Model()


