
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv1  = torch.nn.ConvTranspose2d(3,8,kernel_size=1)

    def forward(self, x):
            v1   = self.conv1(x)
            v2   = v1 + 3
            v4   = v2.clamp_(min=0)
            v5   = v4.clamp_(max=6)
            
            v7   = torch.div(v5 , 6)

            return v7


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1,3,20,20)
