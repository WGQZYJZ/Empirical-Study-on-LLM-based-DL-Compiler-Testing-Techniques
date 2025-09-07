
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
 
    def forward(self, x1):
        split_sizes = (4, 3)
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim=1),  # Concatenate the two first-order tensors in each batch axis
                                            torch.split(torch.cat(x1, dim=0), split_sizes[::-1], dim=1)], dim=2)
        return concatenated_tensor


# Initializing the model
m = Model()


