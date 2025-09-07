
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args): # Allow multiple input tensors to be passed to the forward method 
        res = torch.cat(args, dim=1)
        return res[:, 0:9223372036854775807]


# Initializing the model