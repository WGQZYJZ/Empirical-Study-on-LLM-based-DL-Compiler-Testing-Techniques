
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        split_sizes = [int(input_size / 4)] * 3
        self.split_tensors = torch.split(torch.randn(input_size), split_sizes, dim=0)
 
    def forward(self, x1):
        concatenated_tensor = torch.cat([self.split_tensors[i] for i in range(len(self.split_tensors))], dim=0)
        v6  = self.conv(concatenated_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
        return v6

# Initializing the model
m = Model(input_size)


# Inputs to the model
x1 = torch.randn(2, 3, input_size, input_size)
