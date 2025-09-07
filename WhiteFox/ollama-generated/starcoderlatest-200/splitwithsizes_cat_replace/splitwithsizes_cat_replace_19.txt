
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        # Split tensor along a given dimension into two tensors: one with stride 1 and one with stride 2
        t1_stride1, t2_stride2 = torch.split(x1, split_sizes=[1], dim=0)
        # Concatenate the two tensors along the same dimension to obtain tensor x3
        x3 = torch.cat([t1_stride1, t2_stride2], dim=0)  # [Tensor]
        return x3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 512, 1, 1)
