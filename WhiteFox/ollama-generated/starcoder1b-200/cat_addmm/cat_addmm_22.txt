
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(40, 20)
        self.fc2 = torch.nn.Linear(30, 6)

    def forward(self, x1, x2):
        # TODO: Write your code to generate a valid model
        pass


# Initializing the model
m = Model()

