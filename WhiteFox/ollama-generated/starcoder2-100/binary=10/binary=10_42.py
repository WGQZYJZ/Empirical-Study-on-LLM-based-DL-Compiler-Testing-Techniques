
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(256, 3)
        v2  = v1(x1) + other # <--- the line added in this challenge
        return v2


# Initializing the model