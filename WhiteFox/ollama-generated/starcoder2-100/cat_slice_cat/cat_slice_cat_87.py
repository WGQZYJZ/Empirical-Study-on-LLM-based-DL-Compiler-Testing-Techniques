
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        t_output  = self.conv(x1)
        return t_output

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 3, 576, 900)
 
t1 = torch.cat([x1], dim=1)
t2 = t1[:, :, :, :size]

t4 = torch.cat([t1, t2], dim=1)

 # Initializing the model
m(input_tensors) = t_output
 
