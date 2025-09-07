
class Model(torch.nn.Module):
    def __init__(self, input_size=16, hidden_size=32):
        super().__init__()
 
        # Add two conv layers and a fully connected layer. Each
        self.conv1 = torch.nn.Conv2d(input_size, hidden_size, 1)
        self.conv2 = torch.nn.Conv2d(hidden_size, hidden_size, 3)
        self.fc = torch.nn.Linear(hidden_size*4, 8)
 
    def forward(self, x):
        # Split the tensor to generate two tensors with dimensions (1,28,28) and (1,7,7).
        v1 = self.conv1(x)
        split_tensors = torch.split(v1, split_sizes=(1, 7), dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)
 
        # Add a ReLU function to the output of the convolutional layer and pass it through a two-layer network.
        v2 = torch.nn.functional.relu(concatenated_tensor)
        return self.fc(v2.view(-1, 8))
# Inputs to the model
x1 = torch.randn(1, input_size, input_size)
