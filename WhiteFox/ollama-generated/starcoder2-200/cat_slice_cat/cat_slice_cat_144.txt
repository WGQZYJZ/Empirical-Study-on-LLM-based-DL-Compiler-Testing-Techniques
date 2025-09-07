
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.pool  = torch.nn.AdaptiveAvgPool2d(output_size=(None,))
        self.lin   = torch.nn.Linear(8*64*64, 9223372036854775807)
 
    def forward(self, x1): # x1 must be the first input to the model!
        v1  = self.conv(x1[:,:,:])
        v2  = self.pool(v1)
        v3  = torch.flatten(v2, start_dim=1) 
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model (must be the first input!)
x1  = torch.randn(size=(4096, 8*64*64)) # Shape (batch size, number of classes)
__output__  = m(x1)

