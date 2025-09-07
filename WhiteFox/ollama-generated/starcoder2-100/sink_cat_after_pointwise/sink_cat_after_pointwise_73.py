
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor1, tensor2):
       return torch.cat([tensor1, tensor2], dim=0).view(-1)


# Initializing the model
m = Model()

# Inputs to the model
__input_tensors1__ = torch.randn(3, 5) # Size of each of these tensors is [B, D]
__input_tensors2__ = torch.randn(4, 7)

