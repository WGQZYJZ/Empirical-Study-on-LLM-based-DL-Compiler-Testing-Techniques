
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.linear = torch.nn.Linear(d_in, d_out)
 
    def forward(self, x1):
        return self.linear(x1) - 5


# Initializing the model
m = Model(2, 3)

