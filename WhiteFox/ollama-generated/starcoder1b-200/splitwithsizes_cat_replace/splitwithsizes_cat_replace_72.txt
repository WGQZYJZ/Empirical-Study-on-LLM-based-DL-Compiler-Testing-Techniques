
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[0], 5]  # Split the input tensor into two tensors along a dimension of size 3

        concat_tensors = []
        for i in range(len(split_sizes)):
            concat_tensor = torch.cat([torch.split(x1, split_sizes[i], dim=2)[i], 
                                   torch.split(x1, split_sizes[i], dim=1)[i]], dim=-1)
            concat_tensors.append(concat_tensor)

        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(2, 3, 64, 64)
