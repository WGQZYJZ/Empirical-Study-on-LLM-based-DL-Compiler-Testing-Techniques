
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._conv(x1)
        return torch.relu(v1 + other())
 
other()  # define a public function

# Initializing the model
m = Model()

