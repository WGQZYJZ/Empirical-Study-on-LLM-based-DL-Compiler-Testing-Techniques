
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v1 = torch.matmul(x1[:, :, None], 5*x2[None].transpose(-2, -1))
        v2 = torch.tanh(v1)
        v3 = torch.nn.functional.dropout(v2, p=0.5)
        v4 = 9*torch.tanh(v3*7*v4)

        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(batch_size, 64, 800)  # Batch of 64 sequences with length 800
x2 = torch.randn(7*5*batch_size).view(-1, batch_size, 5)  # A weight tensor that is common to 3 convolutions
x3 = torch.randn(9*8*batch_size).view(-1, batch_size, 8)
x4 = torch.randn(7200*batch_size).view(-1, batch_size, 16)


# Target model
targetModel = Model() # A common pattern here is to have a single initializer for all sub-modules in the model. In this example, a new initializer will be added.

# Initializing the target model
targetModel.__init__()

## Target outputs
