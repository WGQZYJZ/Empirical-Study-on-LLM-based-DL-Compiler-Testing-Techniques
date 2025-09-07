
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = [torch.split(input_tensor, split_sizes, dim) for input_tensor in inputs]
        concatenated_tensor = torch.cat([x for x in split_tensors], dim)
        return True


# Input tensors to the model and the correct sizes of each split tensor
inputs  = [torch.randn(10, 3, 64, 64), torch.randn(2, 5, 128, 128)]
sizes   = [64, 128]

# Model input and output types can be different
m = Model()
