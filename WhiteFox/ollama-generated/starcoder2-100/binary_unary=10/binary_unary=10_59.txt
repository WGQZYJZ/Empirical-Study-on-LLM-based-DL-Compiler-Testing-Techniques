
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v = self.conv1(x1) + self.conv2(x2) if x2 is not None else self.conv1(x1)  # Addition between two convolutions of input tensors
        v = torch.relu(v)  # Apply the ReLU activation function to the output of a linear transformation
        return v


# Initializing the model
m = Model()
 
# Inputs to the model
input_tensor1  = torch.randn(3, 8 , 64, 64)
input_tensor2  = torch.randn(3, 7,  50, 50)
 
# Outputs of the model using the first input tensor and the second one as well
output__ = m(input_tensor1, input_tensor2)
