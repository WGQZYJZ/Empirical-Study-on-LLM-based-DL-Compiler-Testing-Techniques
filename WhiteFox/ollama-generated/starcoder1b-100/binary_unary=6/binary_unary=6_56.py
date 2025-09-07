
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 3  # subtract the value '3' from the output of the linear transformation
        return v1


# Initializing the model
m = Model()


