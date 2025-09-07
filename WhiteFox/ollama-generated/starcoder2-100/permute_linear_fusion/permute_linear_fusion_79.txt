
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3  = x1.permute(0, 4, 1).permute(0, 4, 1) #Pretend to permute more than the 2 dimensions for testing purpose
        v5  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias)
        return v5


# Initializing the model