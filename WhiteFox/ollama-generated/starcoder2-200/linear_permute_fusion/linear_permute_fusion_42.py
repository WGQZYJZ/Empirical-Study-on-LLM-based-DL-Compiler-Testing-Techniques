
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x1):
        v2  = torch.nn.functional.relu(x1, inplace=False) # Apply ReLU to the input tensor.
        v3  = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias) 
        v4 = torch.nn.functional.softmax(v3, dim=0) 
        return v4


# Initializing the model