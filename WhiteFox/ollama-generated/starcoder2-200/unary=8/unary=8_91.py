
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,__unused0__):
        v1 = self.conv(__input__) # Apply pointwise convolution to the input tensor
        return v1

# Initializing the model
m  = Model()

