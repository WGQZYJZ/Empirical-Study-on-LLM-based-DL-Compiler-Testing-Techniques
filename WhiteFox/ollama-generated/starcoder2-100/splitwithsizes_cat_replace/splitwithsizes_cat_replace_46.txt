
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        # split_tensors = torch.split(x1)  # Splitting along batch dimension
        split_tensors = torch.split(x1, [2], dim=0)
        
        # concatenated_tensor = torch.cat(split_tensors)  # Concatenating along batch dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0)
        return 1


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
__output__  = m(x1)