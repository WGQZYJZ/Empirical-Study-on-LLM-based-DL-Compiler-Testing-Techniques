
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1, other=None):
        v1  = self.conv(x1) 
        if (other is not None):
            v2  = v1 + other
        else:
            v2  = v1
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model 
 x1  = torch.randn(1,3,64,64)
 
 # Initialize another tensor for adding with the output of conv operation in forward pass
 other_tensor  = torch.randn(1,8,64,64)
 
 __output__   = m(x1,other=other_tensor)

