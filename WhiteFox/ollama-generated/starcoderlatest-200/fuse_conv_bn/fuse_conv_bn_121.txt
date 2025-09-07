
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1)

    def forward(self, x):
        conv_out = self.conv(x) # Use the functional API in this case
        batch_norm_out = F.batch_norm(conv_out) 
        return batch_norm_out

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 5, 5)
