
class Model(torch.nn.Module):
    def __init__(self, num_features=32, hidden_size=64):
        super().__init__()
        self.fc1 = torch.nn.Linear(num_features, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, num_features)
 
    def forward(self, x):
        # Apply the activation function to x before performing a linear layer with input size 32 and output size 64
        # Add an extra dimension for representing multiple inputs in the model
        t1 = self.relu(self.fc1(x)).view(-1, self.fc1.out_features)
        # Apply the activation function to x before performing a linear layer with input size 64 and output size 32
        # Add an extra dimension for representing multiple inputs in the model
        t2 = self.relu(self.fc2(t1)).view(-1, self.fc2.out_features)
        return t2


# Inputs to the model
x  = torch.randn(4, 3, 64, 64)
y  = x  * 0.5
