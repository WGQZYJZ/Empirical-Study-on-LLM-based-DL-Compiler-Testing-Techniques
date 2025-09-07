
class Model(torch.nn.Module):
    def __init__(self, input_dim):
        super().__init__()

        self.linear  = torch.nn.Linear(input_dim, 2)
        self.relu1   = torch.nn.ReLU()

    def forward(self, x):
        v1 = torch.nn.functional.relu(x + 3 * self.linear(x))
        return v1


# Initializing the model
m = Model(input_dim=2)


# Inputs to the model
x = torch.randn(4096, 8)

__output__|end_of_text| = m(x)

