
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 50)
        self.linear2 = torch.nn.Linear(50, 256)
 
    def forward(self, x):
        x = F.gelu(self.linear1(x))
        x = F.gelu(self.linear2(x))
        return x

# Initializing the model
m = Model()
