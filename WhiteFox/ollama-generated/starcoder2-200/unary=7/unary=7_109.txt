
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 4096)

    def forward(self, x2): 
        v7 = self.linear1(x2) 
        v8 = v7 * clamp(min=0, max=6, v7 + 3) # Multiply the output of the linear transformation by the clamped output (clamped between 0 and 6) of the linear transformation added with `3`
        v9 = v8 / 6 # Divide the output of the multiplication by `6`
        return v9


# Initializing the model