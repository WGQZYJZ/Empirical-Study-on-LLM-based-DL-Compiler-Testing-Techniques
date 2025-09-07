
class Model(torch.nn.Module):
    def __init__(self, neurons_per_layer=[8, 16], leaky_slope=0.2):
        super().__init__()
        self.neurons_per_layer = neurons_per_layer
        self.leaky_slope = leaky_slope
 
        # Define the linear transformation layers
        __layers__ = []
        for index in range(len(self.neurons_per_layer) - 1):
            if index == len(self.neurons_per_layer) - 2:
                __layers__.append(torch.nn.Linear(self.neurons_per_layer[index], self.neurons_per_layer[index + 1]))
            else:
                __layers__.append(torch.nn.Linear(self.neurons_per_layer[index], self.neurons_per_layer[index + 1], bias=False))
 
        # Define the non-linearity function
        self.nonlinearity = torch.nn.LeakyReLU(negative_slope=leaky_slope)
 
    def forward(self, x):
        __layers__ = []
        for index in range(len(self.neurons_per_layer) - 1):
            if index == len(self.neurons_per_layer) - 2:
                __layers__.append(torch.nn.Linear(self.neurons_per_layer[index], self.neurons_per_layer[index + 1]))
            else:
                __layers__.append(torch.nn.Linear(self.neurons_per_layer[index], self.neurons_per_layer[index + 1], bias=False))
        # Apply the non-linearity function to the input tensor
        t4 = self.nonlinearity(x)
        return __layers__

# Initializing the model with the specified hyperparameters
m = Model(leaky_slope=0.2, neurons_per_layer=[8, 16])

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
