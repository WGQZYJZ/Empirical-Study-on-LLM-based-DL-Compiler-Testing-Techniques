
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32768, 512)
        self.relu   = torch.nn.ReLU()
        self.out    = torch.nn.Linear(512, 32)
 
    def forward(self, x):
        v  = self.linear(x)
        w = (self.relu)(v)
        return self.out(w)


# Initializing the model
m  = Model()


