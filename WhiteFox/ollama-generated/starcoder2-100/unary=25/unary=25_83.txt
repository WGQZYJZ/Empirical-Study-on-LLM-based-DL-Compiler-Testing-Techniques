
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope # For each element in v2, if the corresponding element is True, choose the corresponding element from v1 otherwise choose a randomly chosen element from 1.
        v4  = torch.where(v2, v1, v3) 
        return v4

# Initializing the model