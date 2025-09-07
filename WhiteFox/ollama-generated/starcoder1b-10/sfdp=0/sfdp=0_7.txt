
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 50)
 
    def forward(self, x1):
        output = self.linear(x1)
        return output


# Initializing the model
m = Model()


