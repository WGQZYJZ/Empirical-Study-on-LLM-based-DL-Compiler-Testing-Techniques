
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.linear1(x1) + other  # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


