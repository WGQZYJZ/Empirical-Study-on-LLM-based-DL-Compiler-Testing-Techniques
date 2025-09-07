
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1) 
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
__output__  = m(x1)

# Generate a new PyTorch model example
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8,7,stride=4)
 
    def forward(self, x):
        v1  = torch.tanh(x)
        v2  = v1  * -0.5629883
        return v2

# Initializing the model
model  = Model()

 # Inputs to the model
inputs  = torch.randn(4, 3, 257, 257)
 
# Forwarding the inputs through the model and storing outputs
output1  = model(inputs)

# Generate a new PyTorch model example (different from previous model)
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8,7,stride=4)
 
    def forward(self, x):
        v1  = torch.erf(x)
        return v1

# Initializing the model
model  = Model()

 # Inputs to the model
inputs  = torch.randn(4, 3, 257, 257)
 
# Forwarding the inputs through the model and storing outputs
output2  = model(inputs)

# Printing the number of unique items in the outputs of each model (should be different from each other)
print('Unique output values for model1: {}'.format(len(torch.unique(output1))))
print('Unique output values for model2: {}'.format(len(torch.unique(output2))))

# Compare the outputs with regard to precision. The results may vary depending on the randomization of weights and biases. Precision comparison is recommended here.
print('Precision comparison between output1 and output2: {}'.format(torch.allclose(output1, output2)))