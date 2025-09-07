
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # This tensor is concatenated along dimension 0.
        t1 = torch.cat([x1, x1], dim=0)
        # This tensor is reshaped to have more dimensions than input_tensor.
        t2 = t1.view(1, -1)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 2, 2)
