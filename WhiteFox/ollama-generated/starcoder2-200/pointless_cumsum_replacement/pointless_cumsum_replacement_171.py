
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1=70, arg2=56):
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        return m

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, arg1, arg2)

