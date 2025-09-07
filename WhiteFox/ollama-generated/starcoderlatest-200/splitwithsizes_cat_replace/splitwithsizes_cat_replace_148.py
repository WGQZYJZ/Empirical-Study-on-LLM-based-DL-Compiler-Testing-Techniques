
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, [10], dim=1) # Split the input tensor along dimension 1 into 10 tensors of size 64 * 64
        v2 = torch.cat([v1[i] for i in range(len(v1))]) # Concatenate these 10 tensors along dimension 1 to form a single large tensor of shape (num_splits, 64 * 64)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
