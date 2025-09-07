
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + torch.randn_like(v1) / math.sqrt(0.7 * 0.9) # Here the second argument of torch.rand_like is the shape of an input tensor. The tensor with this shape will be created by using the uniform distribution. Then the division operation is performed element-wise on two tensors.
        return v2

# Initializing the model
m = Model()

