
class Model(torch.nn.Module):
    def __init__(self, dim=320):
        super().__init__()

        self.relu = torch.nn.ReLU()

    def forward(self, x1):
       return self.relu(x1.permute(0, 2).view(-1, dim))


# Initializing the model
m = Model()


# Inputs to the model
__input_x1 = torch.randn(48)


