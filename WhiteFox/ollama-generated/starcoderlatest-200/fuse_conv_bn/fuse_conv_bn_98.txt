 
class Model(torch.nn.Module):
    def __init__(self, channels=2):
        super().__init__()

        # Create a list of blocks
        self.blocks = torch.nn.Sequential()
        for c in range(channels):
            self.blocks.add_module('conv' + str(c), torch.nn.ConvXd(...))
            self.blocks.add_module('bn' + str(c), torch.nn.BatchNormXd(...))

        # The output of the last block will be fed into the linear layer
        self.linear = torch.nn.Linear(...)

    def forward(self, x):
        outputs = []
        for b in range(channels):
            inputs  = [x[:, i, :, :, :]] + outputs # The output of ConvXd layer is used as input to BatchNormXd layer.
            outputs += self.blocks[f'bn{b}'](*inputs)

        # The last element in the list should be fed into the linear layer
        out = torch.cat(outputs, dim=1)

        return self.linear(out)


# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
