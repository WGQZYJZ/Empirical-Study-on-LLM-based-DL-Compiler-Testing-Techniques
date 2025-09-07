
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(1024 * 7, 5)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return relu(v1)


# Initializing the model