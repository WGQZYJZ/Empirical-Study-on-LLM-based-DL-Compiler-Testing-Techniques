
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 2048)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1) # Reshape and apply the linear layer to the output of a convolution with kernel size 3 (with stride 2)
        v2 = self.linear(v1) # Reshape and apply the linear layer to the output of the previous layer
        v3 = torch.softmax(torch.matmul(x1, x2.transpose(-1, -2)), dim=-1) # Compute the dot product of the first input with its transpose
        v4 = torch.matmul(v3, v2) # Compute the dot product of the output of the softmax and previous layer
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 768) # The size is [batch size, hidden dimension]
x2 = torch.randn(10, 2048)
