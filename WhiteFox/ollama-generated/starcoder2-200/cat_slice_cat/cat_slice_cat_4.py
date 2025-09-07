
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        v0 = torch.cat([x0, x1], dim=1)
        v1 = v0[:, 0:9223372036854775807]
        v2 = v1[:, 0:size]
        return torch.cat([v0, v2], dim=1)


# Initializing the model
m  = Model()


# Inputs to the model
x0 = torch.randn(batch_size, 3*224//22+1, 64, 64) # batch size * the number of blocks * height of block, width of block (each block contains 5 images)
x1 = x0[:, :9] # the first image of each block in the batch is selected as the input


