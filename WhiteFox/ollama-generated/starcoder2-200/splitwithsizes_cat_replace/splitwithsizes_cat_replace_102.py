
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        self.split = torch.split
        self.concat = torch.cat

    def forward(self, input1):
        splitted = torch.split(input1, [32], 0)
        return self.concat([torch.split(t[0:8]) for t in splitted], 0)[-1]

# Initializing the model
model = Model()

 # Inputs to the model
x1 = torch.zeros((5, 4), dtype=torch.float32)
