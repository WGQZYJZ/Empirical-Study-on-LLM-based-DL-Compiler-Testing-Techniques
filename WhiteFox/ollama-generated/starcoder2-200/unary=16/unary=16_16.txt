
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = nn.Linear(8 * 64 * 64 ,10)
    
    def forward(self, x): 
        v1 = F.relu(self.conv(x))  # Apply the ReLU activation function to a convolutional layer output
        v2 = self.linear(v1.reshape(-1))   # Apply a linear transformation to the output of the ReLU
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(3, 3, 64, 64)
__output__  = m(x)

## How it works:
1. Initialize a Conv-ReLU model with three convolutional layers (in_channels=3), one ReLU layer (out_features=8) and one linear layer to convert the 2D feature map into an output of length 10.

2. Create an input tensor x with dimensions [batch size] = [3, 3, 64, 64].

3. Call the forward method of the model (m(x)) and pass in the input. This runs the forward method of each of the three convolutional layers followed by a ReLU activation function.

4. After applying ReLU to each layer's output, we flatten out the 2D feature maps from [3, 8, 64, 64] into vectors with length 3072 (in_channels * height * width) before running it through a linear transformation followed by a softmax function. The output of this operation is an array of size [batch size = 1] containing probability scores for the classes: {0 to 9}.
