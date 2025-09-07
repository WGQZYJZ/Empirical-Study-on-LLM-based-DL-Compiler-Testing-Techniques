
class Model(torch.nn.Module):
    def __init__(self, args, config=None):
        super().__init__()

        self.layers = nn.ModuleList([])  # List of layers in transformer.

        for i in range(0, len(args)):
            self.layers.append(
                TransformerEncoderLayer(args[i], config['num_heads'],
                                        config['dim'], config['dim']))

    def forward(self, x):
        output = x  # Pass input to the first layer

        for i in range(1, len(self.layers)):
            output = self.layers[i](output)  # Pass output of the previous layer into the next layer

        return output


# Initializing the model
m = Model(args)

