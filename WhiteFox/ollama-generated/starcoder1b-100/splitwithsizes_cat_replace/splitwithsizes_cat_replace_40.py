
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Split the input tensor into several tensors along a given dimension
        # and then concatenate these split tensors along the same dimension.
        split_tensor1 = torch.split(x1, [32, 8], dim=0)  # The first split tensor of dimension 0 will be concatenated to the output of the 0-th split operation in this sequence.
        concat_tensor1 = torch.cat([split_tensor1[0]], dim=0)  # The second split tensor will also be concatenated to the output of the 0-th split operation.
        return self.conv(concat_tensor1)


# Initializing the model
m = Model()


