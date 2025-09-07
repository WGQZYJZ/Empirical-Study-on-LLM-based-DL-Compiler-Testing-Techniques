
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # The input tensor to this model is also a concatenation of 2 tensors
        v1 = torch.cat([x1, x2], dim=0) 
        v2 = v1.view(-1, 1)
        return torch.relu(v2)

# Initializing the model