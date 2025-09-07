
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_size = 16
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes=[1, 4], dim=3)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=3)
        return concatenated_tensor


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
