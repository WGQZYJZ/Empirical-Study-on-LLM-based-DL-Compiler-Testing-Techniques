
class Model(torch.nn.Module):
    def __init__(self, num_splits=2):
        super().__init__()

    def forward(self, x1):
        splits  = torch.split(x1, [50], dim=1) # Split the input tensor into two tensors along dimension one with size 50

        concatenated  = torch.cat([splits[i] for i in range(len(splits))], dim=1) # Concatenate these split tensors along the same dimension

        return concatenated

# Initializing the model and running the forward pass through it on a random input tensor with 2 dimensions of size 8x8:
m = Model()
