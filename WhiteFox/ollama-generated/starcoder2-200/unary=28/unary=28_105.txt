
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        # 78: Linear transformation with 4 input features (the size of the first dimension is equal to batch_size) and 3 output features.
        t1 = torch.nn.functional.linear(x1[:, :, 0], torch.randn(3))

        # 82: Clamping the output of the linear transformation by a minimum value, in this case -1.5
        t2 = torch.clamp_min(t1, min=(-1.5))
 
        # 97: Clamping the previous output to a maximum value
        t3 = torch.clamp_max(t2, max=(0.4))

        return t3
 
m = Model()


# Inputs to the model