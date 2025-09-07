
class Model(torch.nn.Module):
    def __init__(self, num_layers=5):
        super().__init__()

        self.lin1 = torch.nn.Linear(4, 32)
        self.lin2 = torch.nn.Linear(32, 64)
        self.lin3 = torch.nn.Linear(64, 32)
 
        self._layers = nn.ModuleList([self.lin1] + [self.lin2 for _ in range(num_layers - 2)] + [self.lin3])
 
    def forward(self, input):
        output = input.permute(-1, 0).contiguous().view(-1)

        # Iterate over layers and perform matrix multiplication operation on input tensor
        for idx, layer in enumerate(self._layers[:-1]):
            output = torch.nn.functional.linear(output[:, :layer.out_features], layer.weight) + layer.bias
 
        # Perform a concatenation with the last layer's output to get the final model output.
        output = self._layers[-1](torch.cat((input, output), -1))

        return torch.relu6(output).permute(-2, 0).contiguous().view(-1)


# Initializing the model
m = Model()
__outputs__ = m.__outputs__()
 
# Inputs to the model
input_tensor = torch.randn(3456789, 4)
__output__  = __outputs__(input_tensor)