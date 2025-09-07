
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return torch.relu(v1 + other_tensor)


# Initializing the model with a particular input tensor and a particular other tensor
other_tensor  = torch.randn([256])
m  = Model()
x1  = torch.randn([3, 8], dtype=torch.float32)
__output__  = m(x1)

