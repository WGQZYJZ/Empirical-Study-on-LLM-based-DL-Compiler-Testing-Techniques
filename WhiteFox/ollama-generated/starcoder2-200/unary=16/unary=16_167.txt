
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32 * 64, 10)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = torch.relu(v1) # ReLU
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 64 * 64).view(3, 32*64) # view the input tensor in 512 chunks
__output__  = m(x1)

