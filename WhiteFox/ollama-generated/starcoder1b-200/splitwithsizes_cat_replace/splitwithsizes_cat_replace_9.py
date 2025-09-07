
class Model(torch.nn.Module):
    def __init__(self, num_splits=10):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.num_splits = num_splits
 
    def forward(self, x1):
        split_sizes = [int(x1.shape[i] * 0.25) for i in range(len(x1.shape))]
        concatenated_tensor = torch.cat([torch.split(x1, split_sizes, dim=i) for i in range(self.num_splits)], dim=0)
        v1 = self.conv(concatenated_tensor[0])
        return v1


# Initializing the model
m = Model()
