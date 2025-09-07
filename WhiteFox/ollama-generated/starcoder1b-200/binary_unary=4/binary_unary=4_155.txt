
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        if not isinstance(other, torch.Tensor):
            assert False, "The argument 'other' must be a Tensor!"

        v1 = self.linear(x1) + other
        return relu(v1)


# Initializing the model
m = Model()

