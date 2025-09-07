
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 5)
 
    def forward(self, x):
        v1  = self.linear1(x) 
        v3 = v1 + 3 # The clamped version of v1 is added with 3
        v4  = nn.functional.clamp(v3, min=0, max=6)# The clamped version of v1 plus 3 is clamped between 0 and 6
        v5 = v4 / 6 # The output of the clamping process is divided by 6
        return v5

# Initializing the model
m = Model()

