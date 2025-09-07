
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        assert self.is_valid_splitwithsizes_cat((x1, x2, x3)), "Invalid input to the model."

        return torch.cat([
            # split the first 3 tensors along dimension 0 into two tensors and then concatenate them
            # with dimensions in the same order as the original splits for the second 3 tensors
            torch.split(input_tensor, split_sizes, dim=0),

            # split the last 3 tensors along dimension 1 into two tensors and then concatenate them
            # with dimensions in the same order as the original splits for the third 3 tensors
            torch.split(input_tensor, split_sizes, dim=1)
        ], dim=2)

# Initializing the model
m = Model()

