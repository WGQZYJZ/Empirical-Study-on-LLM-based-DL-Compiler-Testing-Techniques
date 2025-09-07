
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x1):
        v1 = x1.view(x1.size(0), -1)  # Reshape the tensor to a 1-d array and add batch dimension
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()

