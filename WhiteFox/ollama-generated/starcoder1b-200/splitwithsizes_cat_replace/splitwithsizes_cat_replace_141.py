
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return self.splitwithsizes_cat([
            self.conv1(x1), # 1.0
            self.conv2(x1) # 0.5
        ])


# Inputs to the model
input_tensor = ... # Generate a valid tensor here
