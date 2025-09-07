
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # This function has been modified for testing purpose
        v2 = torch.relu(x1 + self._bias) 
        return v2

