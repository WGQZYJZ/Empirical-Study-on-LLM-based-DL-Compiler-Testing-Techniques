
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.linear1 = torch.nn.Linear(d_in, d_out)
 
    def forward(self, x):
        return self.linear1(x)


# Initializing the model
m = Model(20, 3)


