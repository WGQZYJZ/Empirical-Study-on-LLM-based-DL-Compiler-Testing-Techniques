
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2, x3], dim=1)
        t2 = t1.view(-1, 9)
        return torch.relu(t2)


# Initializing the model
m = Model()

# Inputs to the model
input_tensors = [torch.randn(1, 2), torch.randn(1, 3), torch.randn(1, 4)]
