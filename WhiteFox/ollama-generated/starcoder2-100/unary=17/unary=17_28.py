
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)

    def forward(self, x1):
        v0 = F.relu(x1)
        return self.conv_transpose(v0)

# Initializing the model
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(1,8,64,64)
 
 