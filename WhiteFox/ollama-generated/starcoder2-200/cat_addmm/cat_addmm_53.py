
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear1  = torch.nn.Linear(784 * 23 + 23, 50)
        self.conv  = torch.nn.Conv2d(1, 96, 3, stride=1, padding=0)
        self.linear2  = torch.nn.Linear(50, dim)
 
    def forward(self, x):
 
        t1  = x.view(-1, 784 * 23 + 23) # Reshape the input to a tensor with dimensions -1 (automatically inferred), 784*23+23
        t2  = self.linear1(t1) # Pass the reshaped input through a linear layer
        t3  = torch.nn.functional.relu(t2) 
        t5  = self.conv(x) # Apply convolution operation to the reshaped input
        t6  = t3 + t5 
        t7  = t6.view(-1, 50).clone() # Reshape the output of the linear layer and copy it as an input for the linear layer again. The input of this layer is a flattened representation of its previous layer’s output.
        t8  = self.linear2(t7) # Apply the linear operation to the output of the convolutional layer

        return t8

# Initializing the model
m1 = Model()


x1  = torch.randn(64, 3 * 23 + 23).clone()
__output__  = m1(x1)

