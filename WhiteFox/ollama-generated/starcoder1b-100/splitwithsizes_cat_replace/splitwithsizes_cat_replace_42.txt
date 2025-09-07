
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        # Do some calculations here.
        split_sizes = [x.shape[3], x.shape[3]]
        concatenated_tensor = torch.cat([
            self.conv1(torch.split(x, split_sizes)[0]),  # Concatenate the first two elements of the input tensor
            self.conv2(torch.split(x, split_sizes)[1])   # Concatenate the second two elements of the input tensor
        ], dim=1)                                      # Concatenate along dimension 1 (first two dimensions)
        return concatenated_tensor


# Initializing the model
m = Model()


