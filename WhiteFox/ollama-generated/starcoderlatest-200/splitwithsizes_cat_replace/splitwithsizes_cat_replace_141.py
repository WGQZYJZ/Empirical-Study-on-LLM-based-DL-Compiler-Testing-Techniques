
class Model(torch.nn.Module):
    def __init__(self, dimension_to_split=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dimension_to_split = dimension_to_split
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [self.conv.kernel_size[self.dimension_to_split], x1.shape[self.dimension_to_split] - self.conv.kernel_size[self.dimension_to_split]], dim=self.dimension_to_split)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=self.dimension_to_split)
        return concatenated_tensor

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 64, 64)
