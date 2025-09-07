
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, 1)
        self.conv2  = torch.nn.ConvTranspose2d(4096, 512, 1)
        self.activation = torch.nn.ReLU()
 
    def forward(self, x):
        v1  = self.conv1(x) 
        v2  = v1  *  0.5
        v3  = v1  *  v1  *  v1 
        v4  = v3  *  0.044715
        v5  = v1 + v4
        v6  = v5  *  0.7978845608028654 
        v7  = self.activation(v6)
        v8  = v7  +  1
        v9  = v2  *  v8

        return v9


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(3, 50000, 64, 64)
__output__  = m(x)