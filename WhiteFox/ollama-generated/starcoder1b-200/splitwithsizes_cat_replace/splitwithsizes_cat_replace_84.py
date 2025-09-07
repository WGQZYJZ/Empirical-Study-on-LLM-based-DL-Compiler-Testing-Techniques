
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes  = [4, 5, 7]
        concatenated_tensor = torch.split(x1, split_sizes, dim=1)  # Split the input tensor into several tensors along a given dimension
        concatenated_tensor[0] = concatenated_tensor[0] + torch.cat([torch.ones((4,), dtype=torch.float), concatenated_tensor[2]], dim=1)  # Concatenate the two outputs of the two split operations along their corresponding dimensions
        return concatenated_tensor[0].detach()


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
