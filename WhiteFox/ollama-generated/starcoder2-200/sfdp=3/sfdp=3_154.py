
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(20, 10)
        self.key   = torch.nn.Linear(30, 50)
 
    def forward(self, v1, v2):
        s  = v2 * scale_factor 
        v10= torch.matmul(v1,s)
        return v1 + 1

# Initializing the model
m = Model()

