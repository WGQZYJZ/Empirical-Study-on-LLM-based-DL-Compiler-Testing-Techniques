
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear0 = torch.nn.Linear(64*64*8, 5)
    
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.flatten(v1, start_dim=1)
        v3 = self.linear0(v2)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model: 64 x 64 x 8 channel input tensor that is fed into the Conv layer and then flattened and used as an input for the Linear Layer.
x1 = torch.randn(1,3,64,64)
__output__  = m(x1)
