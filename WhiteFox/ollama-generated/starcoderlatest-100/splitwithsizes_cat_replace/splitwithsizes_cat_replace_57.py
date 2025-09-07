
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 3, dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)
        return torch.cat((concatenated_tensor), dim=0)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
