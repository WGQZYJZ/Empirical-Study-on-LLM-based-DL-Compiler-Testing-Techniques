
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [2, 3]
        return is_valid_splitwithsizes_cat(
            input_tensor,
            [split_sizes[0], split_sizes[1]],  # Concatenate the first two split tensors along the second dimension
            dim=1)  # Check whether there is only one torch.split operation in the model and one torch.cat operation


# Initializing the model
m = Model()

