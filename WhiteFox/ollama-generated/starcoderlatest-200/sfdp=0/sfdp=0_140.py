
class Attention(torch.nn.Module):
    def __init__(self, dim=None):
        super().__init__()
        self.fc1 = torch.nn.Linear(dim, dim) # Linear layer
        self.fc2 = torch.nn.Linear(dim, dim) # Linear layer
 
    def forward(self, x):
        x1  = F.elu(self.fc1(x)) # Apply ELU activation function to the first linear layer
        x2  = self.fc2(x1) # Apply linear layer to the output of the ELU activation function
        attention_weights = torch.nn.Softmax(dim=-1)(x2) # Compute softmax and apply it to the output of the linear layer
        return attention_weights
class Model(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
        self.layer1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 8, kernel_size=(7, 7), stride=(2, 2), padding=3, bias=False),
            torch.nn.BatchNorm2d(8, track_running_stats=True),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=3, stride=2)
        )
        self.layer2 = Attention(dim * 2) # Apply Scaled Dot-Product Attention with dimension 64
        self.layer3 = torch.nn.Sequential(
            torch.nn.Linear(in_features=80, out_features=1024),
            torch.nn.ReLU(),
        )
 
    def forward(self, x):
        v1 = self.layer1(x) # Apply Convolution 1D and Batch Norm with stride 2 to the input tensor
        v2 = self.layer2(v1).transpose(-2, -1) # Apply Scaled Dot-Product Attention mechanism in the second position of a linear stack to the output of the first Convolution and Batch Norm
        v3 = torch.reshape(v2, [-1, 80]) # Reshape the output of the scaled dot product attention with shape (batch size, no. of heads * head size) into shape (-1, 80). The reshape is done because PyTorch does not provide a native reshape operation
        v4 = self.layer3(v3) # Apply linear layer to the reshaped output of the Scaled Dot-Product Attention
        return v4
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
