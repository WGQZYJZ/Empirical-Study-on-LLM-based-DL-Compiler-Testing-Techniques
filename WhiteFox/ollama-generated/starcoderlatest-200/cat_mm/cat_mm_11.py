
class Model(torch.nn.Module):
    def __init__(self, n_layers=2):
        super().__init__()
        self.n_layers = n_layers

    def forward(self, x1):
        # Concatenate a list of tensors to create an input tensor for each layer
        layers_input = []
        for i in range(self.n_layers):
            if i == 0:
                layers_input.append(x1)
            else:
                layers_input.append(layers_input[i-1])
 
        # Concatenate the list of tensors along a certain dimension
        t2 = torch.cat(layers_input, dim=1)
        return t2
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
