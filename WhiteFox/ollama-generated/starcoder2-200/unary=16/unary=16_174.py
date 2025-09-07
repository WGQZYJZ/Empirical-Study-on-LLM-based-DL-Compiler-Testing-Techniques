
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(2048*7*7, 1536)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(128, 9, 7, 7)
__output__  = m(input_tensor)
