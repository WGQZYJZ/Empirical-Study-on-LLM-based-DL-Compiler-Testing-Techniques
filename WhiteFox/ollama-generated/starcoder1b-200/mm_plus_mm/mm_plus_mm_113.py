
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + torch.mm(x1, x2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 3, 64, 64) # x1: batch_size x channel_num x width x height
x2  = torch.randn(3, 3, 64, 64) # x2: batch_size x channel_num x width x height
