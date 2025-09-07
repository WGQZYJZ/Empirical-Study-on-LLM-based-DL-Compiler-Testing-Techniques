
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 3)

    def forward(self, x1):
        return self.linear(x1) + other # Add another tensor to the output of the linear transformation

# Initializing the model
m = Model()


