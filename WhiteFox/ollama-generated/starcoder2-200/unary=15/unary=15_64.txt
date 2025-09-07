
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply the convolutional layer to the input tensor
        v2  = self.relu(v1)  # Apply the ReLU function to the output of the convolution
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

<p><i>Note: The initial implementation of this task contains a public repository: https://github.com/m0r-ai/m0r-ai-test-pytorch-pointwise-activation-function</i></p>
