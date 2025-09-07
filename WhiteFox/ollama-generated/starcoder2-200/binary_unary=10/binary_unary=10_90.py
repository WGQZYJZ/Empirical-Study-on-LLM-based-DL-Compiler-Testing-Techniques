
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 84 * 50, 6)
 
    def forward(self, x1): 
        v1 = self.linear(x1).view(-1, 84, 6).permute(0, 2, 1)
        v2 = v1 + other # Please add here!
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 84 * 6).view(-1, 32 * 84 * 6) # Please modify here!
