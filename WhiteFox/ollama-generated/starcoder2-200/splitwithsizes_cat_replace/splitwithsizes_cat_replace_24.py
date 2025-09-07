
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [32, 64], dim=0) # split x1 into two tensors of size (32, 64) and concatenate them back using torch.cat()
        return torch.cat([v1[i] for i in range(len(v1))], dim=0)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 32, 64) # x1 has size (64, 32, 64), i.e., it will be split into two tensors of sizes (32, 64) and concatenated back using torch.cat()
