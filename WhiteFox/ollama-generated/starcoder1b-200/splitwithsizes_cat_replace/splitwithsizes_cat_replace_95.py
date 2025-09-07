
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_tensor = torch.split(v1, [4, 2, 2], dim=1)  # Split the output of `conv` along the first dimension
        concatenated_tensor = torch.cat([split_tensor[i] for i in range(len(split_tensor))], dim=0)  # Concatenate the split tensors along the second dimension
        return concatenated_tensor


# Initializing the model
m = Model()


