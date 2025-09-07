
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        split_tensor = torch.split(x, [5], dim=0)  # Split the input tensor into several tensors along dimension 0
        concatenated_tensor = torch.cat([split_tensor[i] for i in range(len(split_sizes))], dim=0)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


