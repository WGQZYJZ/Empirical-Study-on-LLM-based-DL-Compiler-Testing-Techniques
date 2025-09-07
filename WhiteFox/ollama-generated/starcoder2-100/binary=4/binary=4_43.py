
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 7) # Apply a convolutional layer to an input tensor 
        self.conv2 = torch.nn.Conv2d(3, 8, 5)
        self.linear = torch.nn.Linear(49*8*16*16, 1024)
 
    def forward(self, x): # Compute the model output given an input tensor 
        out1 = self.conv1(x)
        out2 = self.conv2(out1)
        out3 = out1 + torch.relu(out2) # Add another layer to the output of the first convolutional layer and apply the ReLU activation function
        out4 = self.linear(torch.reshape(out3, [6*8*5*5])) 
        return out4
 
# Initializing the model
m  = Model()

