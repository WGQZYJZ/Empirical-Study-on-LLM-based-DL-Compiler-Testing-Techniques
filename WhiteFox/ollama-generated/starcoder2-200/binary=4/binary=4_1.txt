
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(64 * 1024, 3)

    def forward(self, x):
        return self.conv(x)

 # Initializing the model
m = Model()

 # Inputs to the model 
 x = torch.rand(size=(1, 64*1024)) 
  