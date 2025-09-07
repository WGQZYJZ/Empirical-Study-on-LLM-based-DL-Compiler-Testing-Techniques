
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(80, 4)
 
    def forward(self, x1):
        v3  = torch.nn.functional.adaptive_avg_pool2d(x1, (65,65)) # Adaptive average pooling: reduces the spatial dimensions to a single number by computing the average of each channel in the previous dimensions
        v4  = v3 / 0.7071067811865476  # Divide the output of adaptive average pooling by 0.7071067811865476
        v5  = torch.nn.functional.gelu(v4) + x1  # Apply gelu to the output of adaptive average pooling, and add it back with the original input tensor
        v7 = self.linear(v5)
        return v7

# Initializing model
mm = MyModel()


# Inputs to the model
x1 = torch.randn(320, 80)
x2 = torch.randn(490, 65)


