
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.relu(x1)  # Apply ReLU operation firstly on an input tensor
        v2 = torch.cat([v1, v1], dim=0).view(-1, 49)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model