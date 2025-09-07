

class Model(torch.nn.Module):
    def __init__(self, num_layers: int=2):
        super().__init__()
        self.conv1 = torch.nn.Conv1d(3, 4, kernel_size=(8)) # Conv1d takes 3 input channels, and 4 output channels as arguments.
        self.conv2 = torch.nn.Conv1d(num_layers * num_layers, 4, kernel_size=7)

    def forward(self, x):
        t1 = x.permute(0, 2, 1).contiguous() # Permute the input tensor with two dims
        t2 = torch.nn.functional.linear(t1,  self.conv2.weight, bias_mat=self.conv2.bias) # Apply linear transformation to the permuted and transposed tensor (using a 4x7 matrix as bias).
        return t2


# Initializing the model