
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [32, 64], dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)
        return torch.tanh(concatenated_tensor)

# Initializing the model
m = Model()

