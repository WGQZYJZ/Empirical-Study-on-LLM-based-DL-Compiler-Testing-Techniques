
class Model(torch.nn.Module):
    def __init__(self, num_layers=2):
        super().__init__()

        self.num_layers  = num_layers
        self.conv1d = torch.nn.Conv1d(3, 4, kernel_size=(1,), stride=1) 
        self.linear   = torch.nn.Linear(200, 50) 

    def forward(self, x):

        out1  = self.conv1d(x).permute((0, 2, 1))
        out2  = self.linear(out1)
        return out2

# Initializing the model
m  = Model()

 # Inputs to the model
 x = torch.randn(5, 3, 200)
__output__  = m(x)


