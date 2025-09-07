
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v2 = torch.cat([x1[:, :3],  # Concatenate two tensors along the first dimension
                        x1[:, [4]], 
                        x1[0:7, ...].view(-1)])  # Re-order tensors using view

        return torch.relu(v2)


# Initializing model