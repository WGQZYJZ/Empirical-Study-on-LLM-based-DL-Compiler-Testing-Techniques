
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(1280, 64) # Linear layer (fully connected neural network with relu activation function and input dimension of 1280 and output dimension of 64.)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(64, 32) # Linear layer (fully connected neural network with relu activation function and input dimension of 64 and output dimension of 32.)
        self.relu2 = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(32, 8) # Linear layer (fully connected neural network with sigmoid activation function and input dimension of 32 and output dimension of 8.)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.linear1(x1) # Apply linear layer to the input tensor 
        v2 = self.relu1(v1) # Use relu activation function on output of previous linear layer
        v3 = self.linear2(v2) # Apply linear layer to the output of previous relu activation function
        v4 = self.relu2(v3) # Use relu activation function on output of previous linear layer
        v5 = self.sigmoid(self.linear3(v4)) # Apply sigmoid activation function on output of previous relu activation function
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 1280)
