
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x2):
        v3 = self.linear(x2) # Linear transformation on input tensor
        v4 = v3.permute(0, 2, 1) 
        return v4

# Initializing the model
m = Model()

