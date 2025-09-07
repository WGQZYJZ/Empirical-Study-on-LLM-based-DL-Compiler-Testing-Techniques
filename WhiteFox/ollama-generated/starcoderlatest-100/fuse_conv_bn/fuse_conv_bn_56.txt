
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)

    def forward(self, x):
        output = self.conv(x)
        return output
    
# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1024, 3, 50)
