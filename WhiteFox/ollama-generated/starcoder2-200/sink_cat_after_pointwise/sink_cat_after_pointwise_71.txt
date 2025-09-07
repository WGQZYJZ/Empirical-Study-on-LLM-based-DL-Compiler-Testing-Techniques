
class Model(torch.nn.Module):
    def __init__(self, num_layers=2):
        super().__init__()

        # Generate a linear transformation layer for each layer of the model
        for i in range(num_layers):
            self.layers = torch.nn.Linear(input_dim, 5)

__output__  = self.layers(x1)

