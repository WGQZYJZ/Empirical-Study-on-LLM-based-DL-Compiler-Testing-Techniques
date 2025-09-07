
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.zeros([32]) 
        v1  = self.conv1(x) + v0 
        v2 = self.conv2(v1) + v0
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
x = torch.randn(3,64,64)
 
__output__  = m(x).detach().cpu().numpy()

