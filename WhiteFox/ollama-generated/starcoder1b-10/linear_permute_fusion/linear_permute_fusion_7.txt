
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = self.linear(x1.permute(0, 2, 1)) # Permute the input tensor with more than 2 dimensions
        return v1


# Initializing the model
m = Model()


