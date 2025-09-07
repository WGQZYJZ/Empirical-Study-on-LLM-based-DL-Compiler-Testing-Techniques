
class Model(torch.nn.Module):
    def __init__(self, input_size, hidden_layers=10):
        super().__init__()
        self._hidden = [torch.nn.Linear(input_size, 32)]

        for _ in range(hidden_layers - 1):
            self._hidden.append(torch.nn.Linear(32, 32))

        self._hidden.append(torch.nn.Linear(32, 8))

    def forward(self, x1):
        v1 = torch.nn.functional.relu(x1)
        for l in self._hidden:
            v1  = torch.nn.functional.linear(v1, l.weight, l.bias)

        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(327680, 512)
__output__  = m(x1)

