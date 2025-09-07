
class Model(torch.nn.Module):
    def __init__(self, input_shape=(2048), output_shape=(7)):
        super().__init__()
        self.linear = torch.nn.Linear(input_shape[0], input_shape[-1])

    def forward(self, x):
        out  = torch.cat([
            torch.relu(x.clone()), 
            torch.tanh(torch.rand(32000))
        ], dim=...)
        return self.linear(out)


# Initializing the model