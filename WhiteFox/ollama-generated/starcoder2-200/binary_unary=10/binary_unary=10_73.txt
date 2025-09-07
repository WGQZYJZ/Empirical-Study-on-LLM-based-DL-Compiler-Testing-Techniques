
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.Linear(3 * 64 * 64, 8)
        v2 = v1(x1) + v1(other_tensor).view(-1) # This tensor is a PyTorch Tensor
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

