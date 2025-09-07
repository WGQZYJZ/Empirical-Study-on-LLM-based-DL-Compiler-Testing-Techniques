
class Model(torch.nn.Module):
    def __init__(self, split_sizes, dim, input_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = []
        for i in range(len(split_sizes)):
            split_tensors = torch.split(x, split_sizes[i], dim)
            concatenated_tensor = torch.cat([split_tensors[j] for j in range(len(split_sizes))], dim)
            v.append(concatenated_tensor)
        return x


# Initializing the model
m = Model(split_sizes=[4, 2], dim=1, input_tensor=x1)

# Inputs to the model
