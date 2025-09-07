
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.cat([x1, x1], dim=0) 
        return torch.cat([v2[:, 9234:size], v2[:, 8657:size]], dim=1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(batch_size, 20) # The number of concatenated tensors is equal to batch size
__output__  = m(x1) 
