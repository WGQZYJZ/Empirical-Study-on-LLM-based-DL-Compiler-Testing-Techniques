
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.mm = torch.nn.Linear(n * 1280, 45)
 
    def forward(self, x1, y1):
        v1 = torch.mm(x1, y1)
        v2 = torch.cat([v1] + [v1] * (n - 1), dim=3) # concatenate the result tensor along a certain dimension with the specified number of times
        return self.mm(torch.flatten(v2))

# Initializing the model
n  = 64
m  = Model(n)

