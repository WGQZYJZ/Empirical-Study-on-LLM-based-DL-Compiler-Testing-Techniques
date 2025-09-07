
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other  # Subtract a tensor or scalar "other" from the output of the convolution
        v3  = torch.relu(v2)  # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v3


# Initializing the model and printing the initial weights as placeholders in the original model. You can initialize it again after we change its first layer's weights so that we know if the updated weights are correct afterwards.

m = Model()

for name, param in m.named_parameters():
    print(name, 'value of parameter:', torch.sum(param))

 # Initializing the model and printing out the initial weights. You can initialize it again after we change its first layer's weights so that we know if the updated weights are correct afterwards.
m = Model()

for name, param in m.named_parameters():
    print(name, 'value of parameter:', torch.sum(param))


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__   = m(x1)
